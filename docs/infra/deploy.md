---
hide:
  - toc
---

# Precisando fazer um deploy? Chegou ao lugar certo

!!! warning "Atenção"
    Os deploys manuais só devem ser feitos nos seguintes casos:
    - Deploy para App
    - Deploy para DevTest
    - Algum teste ou validação em Homologação (Neste caso, se possível, dê preferência às instâncias acima)

## Conecte-se a instância à qual deseja realizar o deploy

!!! tip "Observação"
    Caso não tenha configurado ainda, siga esta etapa antes:<br>
    [Configurando Acesso Remoto](./remote.md)


### 🎈Usaremos como exemplo, a atualização de DevTest

1. Acesse a instância
```bash
# Acessando a instância de homologação
homo
```

2. Acessando a pasta onde se encontra o Script de Deploy
```bash
# Acessando a pasta do script
cd /simbiose/script/shell 
```

3. Rodando o Script de Deploy
!!! info "Observação"
    ###O script precisa receber os seguintes parametros:<br>
    ####Ambiente que será feito o deploy<br>
      1. **ruby-stage**: ambiente de homologação, onde o cliente realiza os testes<br>
      2. **ruby-devtest**: ambiente para teste dos desenvolvedores<br>
      3. **mobile-dev**: ambiente para testes do aplicativo<br>
    ####Branch que será deployada

```bash
# Rodando o Script
# ./update_repo.sh [AMBIENTE] [BRANCH]
./update_repo.sh ruby-devtest feat/minha-branch
```

!!! tip "Observação"
    Se tiver dúvidas sobre qual parâmetro utilizar no deploy, execute o script com o comando abaixo e siga as instruções fornecidas.

```bash
# Rodando o Script
./update_repo.sh
```

Pronto! Seu deploy já está acontecendo, acompanhe o script para observar o andamento!

## Entendendo o fluxo de branch

### Para entender um pouco de como funciona o nosso fluxo, temos este schema representando-o

??? tip "Você também pode acessar por PDF"
    #### Caso seja de sua preferência, você pode visualizar o fluxo por PDF clicando no botão abaixo<br>
    [ CLIQUE AQUI PARA ACESSAR O PDF ](https://drive.google.com/file/d/18_goR3KY-DOlIbYne-u2CVKMD_Ej7P1_/view){ .md-button .md-button--primary target="_blank"}


![Image title](../files/Workflow das Branchs Mercado Topográfico-1.png)
![Image title](../files/Workflow das Branchs Mercado Topográfico-2.png)
![Image title](../files/Workflow das Branchs Mercado Topográfico-3.png)
