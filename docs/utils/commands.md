---
hide:
  - toc
---

# Lista de Comandos Úteis para Trabalhar com Rails
Aqui estão alguns comandos úteis para trabalhar com Rails, organizados por categoria.

???note "Trabalhando com Assets"
    - Realizando a compilação dos assets
    ```bash
    rails assets:precompile
    ```
    - Realizando a limpeza dos assets
    ```bash
    rails assets:clobber
    ```

??? tip "Trabalhando com Migrações"
    - Gerando um novo Model
    ```bash
    # Foo é o nome do Model e da Tabela
    # Bar é uma coluna do tipo String para essa tabela
    rails generate model Foo bar:string
    ```
    - Gerando uma nova migração
    ```bash
    # Criando uma migração adicionando a coluna BAZ e QUX para a tabela Foo
    rails generate migration AddBarAndBazToFoo baz:integer qux:float
    ```
    - Rodando as migrações para o banco
    ```bash
    # [N = Quantidade de migrações para realizar]
    # [Caso STEP não seja passado, irá realizar todas as migrações pendentes]
    rails db:migrate STEP=N
    ```
    - Desfazendo migrações realizadas
    ```bash
    # [N = Quantidade de migrações para desfazer]
    # [Caso STEP não seja passado, irá desfazer somente a última migração]
    rails db:rollback STEP=N
    ```

??? note "Usando o Rails Console"
    - O comando para acessar o Rails console é:
    ```bash
    rails console  # pode ser abreviado para 'rails c'
    ```
    > Com esse comando, ganhamos liberdade para executarmos diversas ações via CLI, por exemplo:
        - Criar, Obter, atualizar, ou destruir dados
            ```bash
            # Já dentro do Rails Console
            user = User.create(name: "John Doe", email: "john@example.com") # Criar um novo dado
            user = User.find(id) # Encontrar um dado
            user.update(email: "john.doe@example.com") # Atualizar um dado
            user.destroy # Apagar um dado
            ```
        - Realizar contagens ou validações
            ```bash
            # Já dentro do Rails Console
            user = User.find_by(email: "john@example.com")
            user.valid? # Verificar se o usuário é válido
            user.errors.full_messages # Verificar mensagens de erro se inválido
            user_count = User.count # Realizar contagem de dados
            ```
        - Carregar partes de código rails
            ```bash
            # Carregar um arquivo Rails
            load 'path/to/file.rb'
            ```
