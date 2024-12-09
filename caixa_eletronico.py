#BANCO PETHRES

print ("BEM VINDO(A) AO BANCO PETHRES, SIGA AS INSTRUÇÕES POR FAVOR! \n")

nome = str(input("Digite seu nome por gentileza:"))
valor_inicial = float(input("Qual será o valor inicial que conterá em sua conta?:"))
print(f"\n SEU DINHEIRO ESTÁ SEGURO CONOSCO {nome}!\n")

opçao = ""

def imprimir_menu():
    print("----------------------------")
    print(">>> | MENU DE OPÇÕES | <<<")
    print("----------------------------")
    print("[1] Sacar")
    print("[2] Depositar")
    print("[3] Extrato")
    print("[0] Sair")
    print("----------------------------")

while opçao != 0:
    imprimir_menu()
    opçao = int(input("Escolha uma opção:"))

    if opçao == 1:
        valor_saque = float(input("Digite o valor que deseja sacar, (OBS: O valor a sacar não pode ser superior ao saldo):"))
        print("Saque em mãos!")
        operação_saque = float (valor_inicial - valor_saque)
        print(f"Saldo atual:R${operação_saque}")

    
    elif opçao == 2:
        valor_depósito = float(input("Digite o valor que deseja depositar:"))
        print("Depositado com sucesso, economizar é essencial!")
        operação_depósito = float(input(valor_depósito + operação_saque))
        print(f"Saldo atual:R${operação_depósito}") 
    
     
    elif opçao == 3:
        print(f"Nome:{nome}")
        print(f"Saldo:R${valor_inicial}")
        print(f"Saques:{valor_saque}") 
        print(f"Depósitos:{valor_depósito}")
        
        
    elif opçao == 0:
        print("Saindo...Até breve no BANCO PETHRES, aguardamos seu retorno assim que precisar!")

    else: print("Opção inválida.")



        

 