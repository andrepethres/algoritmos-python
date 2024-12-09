#lOJA DE CARROS PETHRES

print("Bem vindo(a) a mais nova loja de carros PETHRES, siga as instruções por gentileza!\n")
print("Qual forma de pagameto vai utilizar?")

opçao = ""

def imprimir_menu():
    print("-------------------------------------")
    print(">>> | FORMAS DE PAGAMENTO | <<<")
    print("-------------------------------------")
    print("[1] Dinheiro")
    print("[2] PIX")
    print("[3] Crédito")
    print("[4] Dédito")
    print("[0] Sair")
    print("-------------------------------------")

while opçao != 0:
    imprimir_menu()
    opçao = int(input("Escolha uma opção:\n"))

    if opçao == 1:
        
        #Pagamento
        print("Ok, esperamos sua vinda em nossa loja para efetuar o pagamento")

    elif opçao == 2:
        print("QR CODE")

    elif opçao == 3:

        nome_completo = str (print("Nome e sobrenome:"))
        n_cartao = str (print("Número do cartão:"))
        tipo_cartao = str (print("Tipo do cartão(Visa/Mastercard):"))
        data_val = str (print("Data de validade:"))
        cod_seg = str (print("Código de segurança:"))
        cod_seg = str (print("Código de segurança:"))
        end_pr_cob = str (print("Endereço para cobrança:"))
        end_pr_cob2 = str (print("Endereço para cobrança 2:"))
        city = str (print("Cidade:"))
        estado = str (print("Estado/região:"))
        cep = str (print("CEP:"))
        pais = str (print("País:"))

        print("Cartão cadastrado com sucesso!")

    elif opçao == 4:

        nome_completo = str (print("Nome e sobrenome:"))
        n_cartao = str (print("Número do cartão:"))
        tipo_cartao = str (print("Tipo do cartão(Visa/Mastercard):"))
        data_val = str (print("Data de validade:"))
        cod_seg = str (print("Código de segurança:"))
        cod_seg = str (print("Código de segurança:"))
        end_pr_cob = str (print("Endereço para cobrança:"))
        end_pr_cob2 = str (print("Endereço para cobrança 2:"))
        city = str (print("Cidade:"))
        estado = str (print("Estado/região:"))
        cep = str (print("CEP:"))
        pais = str (print("País:"))


    


        




