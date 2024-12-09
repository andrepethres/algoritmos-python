#lOJA DE CARROS PETHRES

print("Bem vindo(a) a mais nova loja de carros PETHRES, siga as instruções por gentileza!\n")
print("Qual campo deseja fazer seu cadastro?")

#Pedido

opçao = ""

def imprimir_menu():
    print("-------------------------------------")
    print(">>> | PEDIDO | <<<")
    print("-------------------------------------")
    print("[1] Pedido")
    print("[0] Sair")
    print("-------------------------------------")

while opçao != 0:
    imprimir_menu()
    opçao = int(input("Escolha uma opção:\n"))

    if opçao == 1:

        #Pedido
        print("|PEDIDO|\n")
        print("Preencha os requisitos\n")
        marca = str(input("Digite a marca:"))
        modelo = str(input("Modelo:"))
        cor = str(input("Cor:"))
        ano_mod = str(input("Ano modelo:"))
        potencia = str(input("Potência(Motor):"))
        tipo = str(input("Tipo(Novo, seminovo, usado):"))
        faixa_km = str(input("Faixa de km rodados:"))
        combustivel = str(input("Combustível:"))
        portas = str(input("Portas:"))
        ar_cond = str(input("Ar condicionado:"))
        trava_vidros = str(input("Trava e vidros:"))
        direcao = str(input("Direção:/n"))
        print("Pedido enviado com sucesso!")

    elif opçao == 0:
        print("Saindo...Até breve, aguardamos seu retorno assim que precisar!")

    else: print("Opção inválida.")