# language: pt

Funcionalidade: Exemplo de testes de interface

  Esquema do Cenário: Validar soma de 2 números
    Dado que eu acesse o site "https://www.lambdatest.com/selenium-playground/simple-form-demo"
    Quando eu informar <primeiro_numero> no primeiro campo
    E eu informar <segundo_numero> no segundo campo
    E clicar no botão "Get values"
    Então o resultado será <somatorio>
    Exemplos:
      | primeiro_numero | segundo_numero | somatorio |
      | 1               | 2              | 3         |
      | 5               | 12             | 17        |
      | 10              | 15             | 25        |
      | 50              | 1              | 51        |
      | 38              | 12             | 50        |