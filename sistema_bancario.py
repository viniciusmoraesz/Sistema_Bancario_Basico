menu_opcoes = """

                               *********SEJA BEM VINDO!***********
                               
                               *******ESCOLHA UMA OPÇÃO***********

                               [1] - Depositar
                               [2] - Sacar
                               [3] - Checar Extrato
                               [4] - Sair do Sistema
                                    
"""

saldo = 0
limite_maximo_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def funcao_deposito():
    global saldo
    deposito = float(input("Quanto dinheiro você deseja depositar? \n"))


    if deposito > 0:
            saldo += deposito
            extrato.append(f"Depósito: R${deposito:.2f}")
            print(f"Você depositou R${deposito:.2f}")
    else:
            print("É necessário depositar um valor acima de R$ 0,00")



def funcao_sacar():
      global saldo
      global limite_maximo_saque
      global numero_saques
      global LIMITE_SAQUES

      saque = float(input("Quanto dinheiro você deseja sacar? \n"))

      if saque > saldo:
            print("Não é possível realizar o saque, saldo insuficiente!")
      elif saque > limite_maximo_saque:
            print("Não é possível realizar o saque, o limite máximo para um saque é de R$ 500,00!")  
      elif numero_saques >= LIMITE_SAQUES:
            print(f"Não é possivel realizar mais saques, o número máximo de saques diários é de {LIMITE_SAQUES}")
      else:
            saldo -= saque
            numero_saques += 1
            extrato.append(f"Você sacou R${saque:.2f}")
            print(f"Você sacou R${saque:.2f}")             


def funcao_extrato():
      if not extrato:
            print("Você não realizou nenhuma ação! \n")
      else:
            print("Todo o seu extrato bancário abaixo! \n")  

            for transacao in extrato:
                  print(transacao)
            print(f"O seu saldo atual é de: R${saldo:.2f}")          
      

def funcao_sair():
      print("Você está deixando o sistema. Até logo!")
      
                  



while True:

    opcao = int(input(menu_opcoes))

    if opcao == 1:
          funcao_deposito()
    elif opcao == 2:
          funcao_sacar()
    elif opcao == 3:
          funcao_extrato()
    elif opcao == 4:
          funcao_sair()
          break
    else:
          print("Opção Inválida. Tente novamente")      
                
                


