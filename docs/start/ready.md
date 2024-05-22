---
hide:
  - toc
---


# Instalação, configuração e inicialização do projeto Mercado Topográfico

## Como nos organizamos?
### Atualmente o nosso backend está separado de forma modular, ou seja, cada pedacinho é responsável por uma parte específica do comportamento, para que o cliente possa ter a liberdade de habilitar ou desabilitar novos módulos.

## Nossos Módulos
<details>
  <summary>Auth</summary>
  <p>Este módulo é utilizado para autenticação dos usuários, e junto de uma tabela de permissionamento, define quais os acessos que aquele usuário pode ter</p>
  <p>Contamos também com um atributo de "Salt" para gerenciar recuperações de senha ou ativações de usuário, fazendo assim com que o link seja inválidado após o uso.</p>
</details>
<details>
  <summary>Home</summary>
    <p>O módulo Home atualmente conta com uma simples rota que retorna o host do usuário, sendo utilizado para ver se realmente o host cadastrado no cliente está sendo retornado da forma correta antes de adicionar novas alterações.</p>
</details>
<details>
  <summary>Projects</summary>
  <p>O módulo de Projetos é utilizado para o cadastro e gerenciamento de projetos do time, atualmente conta com um cadastro simplificado e gera os dados de pagamento fictícios diretamente no banco de dados.</p>
</details>
<details>
  <summary>S3</summary>
  <p>O módulo do S3 realiza uploads vinculando-os a uma pasta única do cliente dentro da Amazon, o que facilita o controle de arquivos do mesmo sem interferir em outros clientes.</p>
</details>
<details>
  <summary>Settings</summary>
  <p>O módulo de configurações atualmente é capaz de definir os parametros de Cores, logos e banners do cliente, bem como alguns textos chaves.</p>
</details>
<details>
  <summary>Users</summary>
  <p>O módulo de Usuários é um dos corações do sistema, já possui barreiras de permissionamentos e uma gama de testes para garantir sua integridade.</p>
</details>

## Desafios concluídos
<details>
  <summary>Arquitetura</summary>
  <p>A Nossa arquitetura de multi-tenants está muito bem estruturada no momento, simplificando criação, manutenção e deleção de novos clientes.</p>
  <p>O Nosso sistema de versionamento do banco de dados também garante segurança dos dados e apontamento correto para onde determinado model deve ser criado, mantendo também um histórico de data/hora de cada modificação gerada.</p>
</details>
