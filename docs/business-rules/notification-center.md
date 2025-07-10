# Regras de Negócio para a Central de Notificações do Mercado Topográfico

Este documento descreve em detalhes a arquitetura e regras de negócio relacionadas ao envio de notificações push utilizando a infraestrutura do Expo, integrada ao backend em Ruby on Rails e processamento assíncrono com Sidekiq. O sistema foi projetado para funcionar tanto com usuários autenticados quanto com visitantes não logados (guests). Isso permite, por exemplo, que um usuário que ainda não fez login receba notificações contextuais, como promoções, avisos de geolocalização ou mensagens relacionadas a ações anônimas no aplicativo, desde que o token do dispositivo esteja registrado.

---

## 1. Visão Geral

A central de notificações push foi projetada para ser robusta, escalável e de fácil manutenção. Seu objetivo é:

- **Receber** solicitações de envio de notificações a partir de diversos pontos da aplicação (API, tarefas agendadas, etc.).
- **Processar** lotes de tokens para otimizar chamadas externas e respeitar limites de rate-limit.
- **Enviar** efetivamente as notificações usando o serviço Expo, tratando erros e mantendo o estado dos tokens.

Cada classe tem responsabilidade única dentro desse fluxo, evitando acoplamentos e facilitando testes.

## 2. Arquitetura e Fluxo de Execução

### **Trigger**

O fluxo de envio de notificações push começa com um **trigger** **(gatilho)**, que representa o ponto de entrada inicial do fluxo de notificações. Esse trigger pode estar em um endpoint da API, Controller ou qualquer outro método da aplicação que o suporte. Um trigger pode ser um evento disparado pela aplicação, como login, cadastro ou finalização de compra. Sua principal responsabilidade é acionar a cadeia de envio de notificação para um usuário afetado. Ele faz isso chamando `Dispatcher.for_user`, passando o título, corpo da mensagem, dados adicionais e o usuário alvo. O Dispatcher então se encarrega de continuar o fluxo de forma assíncrona e segura.

**Exemplo prático:**

```ruby
post '/login' do
  # Após autenticação bem-sucedida
  ::Utils::Notification::Dispatcher.for_user(
    user,
    'Login realizado com sucesso',
    "Olá, #{user.name}, seu login foi efetuado com êxito!",
    { event: 'user_login', screen: '/' }
  )
end
```

Esse código dispara imediatamente o fluxo de notificação quando o login é bem-sucedido.

### **Dispatcher**

Em seguida, o **Dispatcher** é responsável por filtrar os tokens ativos do usuário, ou seja, aqueles com `active = true` no modelo `ExpoPushToken`. Ele remove tokens inativos para evitar erros e, caso existam tokens válidos, enfileira um `ExpoNotificationWorker` com os dados da notificação.

**Exemplo prático:**

Um mesmo usuário pode ter múltiplos tokens salvos no sistema porque cada instalação do aplicativo (em diferentes dispositivos ou após reinstalações) gera um novo token de push. Por exemplo, se o usuário acessa o app pelo celular e também pelo tablet, ele terá dois tokens distintos. Além disso, uma reinstalação do app em um mesmo dispositivo também pode gerar um token novo, mantendo o anterior (que pode se tornar inativo posteriormente). Sendo assim, se um usuário tiver 3 tokens salvos, mas apenas 2 forem ativos (isto é, com `active = true`), apenas esses dois serão considerados para envio de notificações.

### **ExpoNotificationWorker e ExpoNotificationBatchWorker**

O **ExpoNotificationWorker** é o worker principal responsável por coordenar o envio em lote das notificações. Ele é acionado pelo `Dispatcher` e serve como intermediário entre a coleta de tokens e a delegação do envio ao Expo.

Este worker é importante para tratar falhas de rede da própria máquina onde o Sidekiq está rodando. Por exemplo, se houver uma queda temporária da conexão a internet ou problemas de DNS na instância do servidor, o retry automático do Sidekiq tentará reenviar os jobs posteriormente.

Além disso, ele divide os tokens recebidos em subgrupos com o tamanho definido por `BATCH_SIZE`, garantindo que cada subgrupo de tokens seja enviado de forma controlada e escalável. Para cada subgrupo, ele enfileira um job `ExpoNotificationBatchWorker`, que é responsável por tratar falhas de envio à API do Expo propriamente dita.

Portanto, a separação entre `ExpoNotificationWorker` e `ExpoNotificationBatchWorker` garante resiliência em dois níveis:

- **ExpoNotificationWorker**: trata falhas de infraestrutura local (ex: perda de conexão, erro de DNS).
- **ExpoNotificationBatchWorker**: trata falhas na comunicação com a API da Expo (ex: erro 429 por excesso de requisições ou erro 500 por falha interna da Expo), garantindo tentativas de reenvio e tratamento adequado dos tokens inválidos.

Essa arquitetura modular facilita debug, observabilidade e garante maior confiabilidade no processo de envio.

Voltando ao fluxo, o **ExpoNotificationWorker** então assume o controle. Ele gera um `notification_id` único, que será usado como identificador comum entre todos os lotes gerados a partir daquela solicitação de envio. Esse identificador é essencial para rastrear, agrupar e diagnosticar o envio nos logs e dashboards de monitoramento, pois permite saber exatamente quais lotes pertencem a uma mesmo disparo.

Em seguida, o worker divide os tokens em lotes de tamanho definido por `BATCH_SIZE`, e para cada lote, enfileira um `ExpoNotificationBatchWorker`. Cada um desses lotes carrega consigo o `notification_id` e também um `batch_index` indicando a sua posição na sequência de envio.

**Exemplo prático:**

1000 tokens resultarão em 10 batches se `BATCH_SIZE` for 100.

### **ExpoNotificationService**

Cada ExpoNotificationBatchWorker recebe um lote específico e cria a instância do **ExpoNotificationService**, que é responsável pela lógica de comunicação com a API do Expo. Ele chama o método `call`, que por sua vez divide novamente os tokens (se necessário), monta as mensagens no formato correto, envia ao Expo, trata os erros de forma resiliente (com retry exponencial) e atualiza os estados dos tokens no banco, desativando tokens inválidos.

**Exemplo prático:**

Um lote pode conter tokens que não estão mais válidos. O serviço irá identificar esses tokens, marcar como inativos no banco, e seguir com o restante normalmente.

### **ExpoPushToken (model)**

Por fim, o modelo **ExpoPushToken** representa o token de notificação associado a um usuário. Ele permite ativar, desativar e consultar o status dos tokens de forma performática. Também mantém o histórico de uso, com o campo `last_used_at`, que é atualizado a cada envio bem-sucedido.

## 3. Sequência de Chamadas

1. `Dispatcher.for_user(user, title, body, data)`

   - Ponto de entrada inicial do fluxo. Recebe os parâmetros de notificação e filtra os tokens ativos do usuário. Caso existam tokens válidos, enfileira o `ExpoNotificationWorker`.

2. `ExpoNotificationWorker.perform(tokens, title, body, data)`

   - Gera um `notification_id` único e divide os tokens em lotes. Para cada lote, enfileira um `ExpoNotificationBatchWorker` com os dados do lote.

3. `ExpoNotificationBatchWorker.perform(batch_tokens, title, body, data)`

   - Instancia o `ExpoNotificationService` e chama o método `call` para enviar as notificações.

4. `ExpoNotificationService.call`

   - Realiza a comunicação com a API do Expo, aplicando retry exponencial e tratando respostas. Atualiza o estado dos tokens no banco.

5. `ExpoPushToken`

   - Modelo responsável por representar os tokens no banco de dados e manter seu estado (ativo/inativo) e histórico de uso.


```
[API Trigger] 
    -> Dispatcher.for_user
        -> ExpoNotificationWorker.perform_async
            -> perform
                -> ExpoNotificationBatchWorker.perform_async (para cada lote)
                    -> perform
                        -> ExpoNotificationService.call
                            -> process_tokens_in_batches
                                -> send_messages_with_retry
```

*Nota*: a dupla divisão em lotes (no worker e no service) garante proteção dupla e flexibilidade de tamanhos diferentes.

## 4. Endpoints `app/api/v1/routes/push_tokens.rb`

A API disponibiliza dois endpoints principais para o registro de tokens de notificação no backend:

- **POST `/push_tokens/guest`**: utilizado quando o usuário ainda **não está autenticado**. Essa rota associa o token ao dispositivo de forma anônima (sem `user_id`).

- **POST `/push_tokens`**: rota protegida por autenticação. Deve ser usada quando o usuário **já está logado**. O token será vinculado ao `user_id` atual no banco de dados.

Ambas as rotas utilizam `ExpoPushToken.find_or_initialize_by(token:)` para evitar duplicidade de registros, permitindo também que tokens existentes sejam atualizados com novos dados, como `last_used_at` ou `user_id`.

## 5. Integração com o Frontend

No app React Native (usando o Expo), o fluxo de registro de token é feito em três etapas principais:

1. Captura do token:

```tsx
import * as Notifications from 'expo-notifications';

const registerForPushNotificationsAsync = async () => {
  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') return;

  const tokenData = await Notifications.getExpoPushTokenAsync();
  return tokenData.data; // Este é o expoPushToken
};
```

2. Decisão da rota:

Verifica-se se o usuário está logado (via contexto de autenticação) e escolhe qual endpoint chamar:

```tsx
if (user?.token) {
  await api.post('/push_tokens', { token: expoPushToken });
} else {
  await api.post('/push_tokens/guest', { token: expoPushToken });
}
```

3. Armazenamento local e controle:

Atualiza-se o `AsyncStorage` ou o estado global do app com o array de tokens retornado pela API para uso futuro e exibição nas configurações de dispositivo, se necessário.
