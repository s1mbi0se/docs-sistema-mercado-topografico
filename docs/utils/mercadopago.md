## Mercado Pago - Chile

### Documentação
* <a href="https://www.mercadopago.com.br/developers/pt/reference" target="_blank">Documentação Mercado Pago</a>

### Cartões de teste

|Cartão|Número|Código de segurança   |Data de vencimento|
|---|---|---|---|
| Mastercard  | 5416 7526 0258 2580  | 123  | 11/25  |
| Visa  | 4168 8188 4444 7115  | 123  |  11/25 |
|  American Express | 3757 781744 61804  | 1234  |  11/25 |



### Status de pagamento 
(Para testar diferentes resultados de pagamento, insira o status desejado no nome do titular do cartão:)

| Status de pagamento  |  Descrição | Documento de identidade  |
|---|---|---|
| APRO  |  Pagamento aprovado |  (outro) 123456789 |
|  OTHE |  Recusado por erro geral |   |
| CONT  | Pagamento pendente  | -  |
|  CALL |  Recusado com validação para autorizar | -  |
| FUND  | Recusado por quantia insuficiente  | -  |
|  SECU | Recusado por código de segurança inválido  |  - |
| EXPI  |  Recusado por problema com a data de vencimento |  - |
| FORM  |  Recusado por erro no formulário | -  |
