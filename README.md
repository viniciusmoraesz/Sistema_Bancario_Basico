# 🌟 **Sistema Bancário em Python** 🌟

Este projeto consiste em um sistema bancário desenvolvido em Python, incorporando funcionalidades essenciais como depósito, saque e consulta de extrato. Durante o desenvolvimento, apliquei conceitos fundamentais aprendidos no **bootcamp**, incluindo:

- 🛠️ **Funções**
- 🔄 **Estruturas de repetição** (`for` e `while`)
- ➗ **Operadores**
- 🧩 **Estruturas condicionais** (`if`, `else`, `elif`)

## 🚀 **Funcionalidades** 🚀

- 💰 **Depósito:** Permite ao usuário adicionar fundos à sua conta, atualizando o saldo e registrando a transação no extrato.
- 💸 **Saque:** Facilita a retirada de valores, garantindo que o saldo seja suficiente e que o número máximo de saques diários não seja excedido, além de ter um limite máximo de retirada individual. Também registra a transação no extrato.
- 📝 **Extrato:** Exibe um histórico completo de todas as transações realizadas, incluindo depósitos e saques, juntamente com o saldo atual.

## 🧩 **Estrutura do Código** 🧩

### 🌐 **Variáveis Globais** 🌐

- `saldo`: 💵 Armazena o saldo atual da conta.
- `limite_maximo_saque`: 💳 Define o valor máximo permitido para saques individuais.
- `extrato`: 🗃️ Lista que mantém o histórico de todas as transações.
- `numero_saques`: 🔢 Contabiliza o número de saques realizados no dia.
- `LIMITE_SAQUES`: 📊 Estabelece o número máximo de saques permitidos por dia.

### 🛠️ **Funções** 🛠️

- `funcao_deposito()`: 💸 Solicita ao usuário um valor para depósito, valida a entrada e atualiza o saldo e o extrato.
- `funcao_sacar()`: 💰 Permite ao usuário realizar um saque, verificando condições como saldo suficiente e limite de saques diários; atualiza também o extrato.
- `funcao_extrato()`: 📝 Exibe todas as transações registradas no extrato e o saldo atual.
- `funcao_sair()`: 🚪 Finaliza a execução do programa com uma mensagem de despedida.

## 🎯 **Conclusão** 🎯

Este projeto foi desenvolvido com o objetivo de consolidar os conhecimentos adquiridos no bootcamp, aplicando conceitos fundamentais de programação para criar um sistema funcional e intuitivo. O código pode ser expandido com novas funcionalidades, como transferência entre contas, aplicação de juros, entre outros, conforme o desenvolvimento de habilidades avançadas.

---

*Este README foi elaborado com o auxílio do [readme.so](https://readme.so/pt) para proporcionar uma estrutura clara e organizada.* 😊
