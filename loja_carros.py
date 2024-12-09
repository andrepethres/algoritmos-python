#lOJA DE CARROS PETHRES

print("Bem vindo(a) a mais nova loja de carros PETHRES, siga as instruções por gentileza!\n")
print("Qual campo deseja fazer seu cadastro?")

opçao = ""

def imprimir_menu():
    print("-------------------------------------")
    print(">>> | MENU DE OPÇÕES CADASTRAIS | <<<")
    print("-------------------------------------")
    print("[1] Cadastro vendedor")
    print("[2] Cadastro cliente")
    print("[3] Cadastro carro")
    print("[0] Sair")
    print("-------------------------------------")

while opçao != 0:
    imprimir_menu()
    opçao = int(input("Escolha uma opção:"))

    if opçao == 1:

        #Cadastro vendedor
        print("|DADOS PESSOAIS|\n")
        nome_completo = str(input("Digite seu nome completo por gentileza:"))
        nome_usuario = str(input("Digite seu novo nome de usuário:"))
        senha = str(input("Crie uma senha:"))
        confirma_senha = str(input(f"Confirme sua senha: {senha}"))
        print("ATENÇÂO!Anotou seu nome de usuário e nova senha? Deixe anotado para não esquecer, isso é de extrema importância para fazer login ao entrar novamente no sistema!Continue seu cadastro.")
        rg = str(input("RG:"))
        cpf = str(input("CPF:"))
        data_nasc = str(input("Data de nascimento:"))
        email = str(input("E-mail:"))
        tel = str(input("Telefone:\n"))
        print("|ENDEREÇO|\n")
        rua = str (input("Rua:"))
        complemento = str(input("Complemento:"))
        cidade = str(input("Cidade:"))
        uf = str(input("Estado:\n"))

        print("Cadastro realizado com sucesso, seus dados estão seguros conosco!")
    
    elif opçao == 2:

        #Cadastro cliente
        print("|DADOS PESSOAIS|\n")
        nome_completo = str(input("Digite seu nome completo por gentileza:"))
        nome_usuario = str(input("Digite seu novo nome de usuário:"))
        senha = str(input("Crie uma senha:"))
        confirma_senha = str(input(f"Confirme sua senha: {senha}"))
        print("ATENÇÂO!Anotou seu nome de usuário e nova senha? Deixe anotado para não esquecer, isso é de extrema importância para fazer login ao entrar novamente no sistema!Continue seu cadastro.")
        rg = str(input("RG:"))
        cpf = str(input("CPF:"))
        data_nasc = str(input("Data de nascimento:"))
        email = str(input("E-mail:"))
        tel = str(input("Telefone:\n"))
        print("|ENDEREÇO|\n")
        rua = str (input("Rua:"))
        complemento = str(input("Complemento:"))
        cidade = str(input("Cidade:"))
        uf = str(input("Estado:\n"))

        print("Cadastro realizado com sucesso!Seus dados estão seguros conosco, agora você é o mais novo cliente da nossa loja, sinta-se a vontade!")
        
    elif opçao == 3:

        #Cadastro carro
        print("|DADOS DO CARRO|\n")
        marca = str(input("Digite a marca:"))
        modelo = str(input("Modelo:"))
        placa = str(input("Placa:"))
        cor = str(input("Cor:"))
        ano_fab = str(input("Ano fabricação:"))
        ano_mod = str(input("Ano modelo:"))
        potencia = str(input("Potência(Motor):"))
        tipo = str(input("Tipo(Novo, seminovo, usado):"))
        km = str(input("Km rodados:"))
        renavam = str(input("N° Renavam:"))
        combustivel = str(input("Combustível:"))
        preco_compra = str(input("Preço compra:"))
        preco_venda = str(input("Preço venda:"))
        cidade_uf = str(input("Cidade-UF:"))
        portas = str(input("Portas:"))
        ar_cond = str(input("Ar condicionado:"))
        trava_vidros = str(input("Trava e vidros:"))
        direcao = str(input("Direção:/n"))
        print("|CHECK-LIST|")
        manual = str(input("Manual:"))
        chave_reserva = str(input("Chave reserva:"))
        step = str(input("Step:"))
        triangulo = str(input("Triângulo:"))
        macaco = str(input("Macaco:"))
        chave_roda = str(input("Chave de roda:"))
        status = str(input("Status(Disponível ou indisponível):"))
        data_entrada = str(input("Data entrada:"))
        data_saida = str(input("Data saída:"))
        print("|STATUS|")
        mecanica = str(input("Mecânica:"))
        lavacao = str(input("Lavação:"))
        fipe = str(input("Tabela FIPE:\n"))

        print("Cadastro realizado com sucesso!")
        
    elif opçao == 0:
        print("Saindo...Até breve, aguardamos seu retorno assim que precisar!")

    else: print("Opção inválida.")

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
        

