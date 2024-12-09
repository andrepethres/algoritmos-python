class Cliente:

    def __init__(self, id_cliente="", nome_completo="", nome_usuario="", data_nasc="", login="", senha="", confirma_senha="", rg="", cpf="", cnh="", email="", telefone="", cidade="", estado="", cep="", rua="", numero_casa="", complemento="", ativo="", inativo=""):
        self._id_vendedor = id_cliente
        self._nome_completo = nome_completo
        self._nome_usuario = nome_usuario
        self._data_nasc = data_nasc
        self._login = login
        self._senha = senha
        self._confirma_senha = confirma_senha
        self._rg = rg
        self._cpf = cpf
        self._cnh = cnh
        self._email = email
        self._telefone = telefone
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
        self._rua = rua
        numero_casa = numero_casa
        self._complemento = complemento
        self._ativo = ativo
        self._inativo = inativo

    def get_id_cliente(self):
        return self._id_cliente
    
    def set_id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    def get_nome_completo(self):
        return self._nome_completo
    
    def set_nome_completo(self, nome_completo):
        self._nome_completo = nome_completo

    def get_nome_usuario(self):
        return self._nome_usuario
    
    def set_nome_usuario(self, nome_usuario):
        self._nome_usuario = nome_usuario

    def get_data_nasc(self):
        return self._data_nasc
    
    def set_data_nasc(self, data_nasc):
        self._data_nasc = data_nasc
    
    def get_login(self):
        return self._login
    
    def set_login(self, login):
        self._login = login

    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha = senha

    def get_confirma_senha(self):
        return self._confirma_senha
    
    def set_confirma_senha(self, confirma_senha):
        self._confirma_senha = confirma_senha

    def get_rg(self):
        return self._rg
    
    def set_rg(self, rg):
        self._rg = rg
    
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_cnh(self):
        return self._cnh
    
    def set_cnh(self, cnh):
        self._cnh = cnh

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email= email

    def get_telefone(self):
        return self._telefone
    
    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_cidade(self):
        return self._cidade
    
    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado

    def get_cep(self):
        return self._cep
    
    def set_estado(self, cep):
        self._cep = cep

    def get_rua(self):
        return self._rua
    
    def set_rua(self, rua):
        self._rua = rua

    def get_numero_casa(self):
        return self._numero_casa
    
    def set_numero_casa(self, numero_casa):
        self._numero_casa = numero_casa

    def get_complemento(self):
        return self._complemento
    
    def set_complemento(self, complemento):
        self._complemento = complemento

    def get_ativo(self):
        return self._ativo
    
    def set_ativo(self, ativo):
        self._ativo = ativo

    def get_inativo(self):
        return self._inativo
    
    def set_inativo(self, inativo):
        self._inativo = inativo

    def cadastrar_cliente(self):
        print(">>>CADASTRE-SE<<<\n")
        print("|DADOS PESSOAIS|\n")
        self._id = input("ID cliente:")
        self._nome_completo = input("Digite seu nome completo:")
        self._nome_usuario = input("Crie seu nome de usuário:")
        self._data_nasc = input("Data de nascimento:")
        self._login = input("Login(Digite seu nome de usuário):")
        self._senha = input("Crie uma senha somente com números:")
        self._confirma_senha = input("Confirma senha(Digite novamente):\n")
        print("ATENÇÂO!Anotou seu nome de usuário e nova senha? Deixe anotado para não esquecer, isso é de extrema importância para fazer login ao entrar novamente no sistema!Continue seu cadastro.\n")
        self._rg = input("RG:")
        self._cpf = input("CPF:")
        self._cnh = input("Quais CNHs você possui?:")
        self._email = input("E-mail:")
        self._telefone = input("Telefone:\n")
        print("|ENDEREÇO|\n")
        self._cidade = input("Cidade:")
        self._estado = input("Estado:")
        self._cep = input("CEP:")
        self._rua = input("Rua:")
        self.numero_casa = input("N°:")
        self._complemento = input("Complemento:\n")
        self._ativo
        self._inativo 
        print("Cadastro efetuado com sucesso!\n")
        

    def atualizar_cad_cliente(self):
        print(">>>CADASTRE-SE<<<\n")
        print("|DADOS PESSOAIS|\n")
        self._id = input("ID cliente:")
        self._nome_completo = input("Digite seu nome completo:")
        self._nome_usuario = input("Crie seu nome de usuário:")
        self._data_nasc = input("Data de nascimento:")
        self._login = input("Login(Digite seu nome de usuário):")
        self._senha = input("Crie uma senha somente com números:")
        self._confirma_senha = input("Confirma senha(Digite novamente):\n")
        print("ATENÇÂO!Anotou seu nome de usuário e nova senha? Deixe anotado para não esquecer, isso é de extrema importância para fazer login ao entrar novamente no sistema!Continue seu cadastro.\n")
        self._rg = input("RG:")
        self._cpf = input("CPF:")
        self._cnh = input("Quais CNHs você possui?:")
        self._email = input("E-mail:")
        self._telefone = input("Telefone:\n")
        print("|ENDEREÇO|\n")
        self._cidade = input("Cidade:")
        self._estado = input("Estado:")
        self._cep = input("CEP:")
        self._rua = input("Rua:")
        self.numero_casa = input("N°:")
        self._complemento = input("Complemento:\n")
        self._ativo
        self._inativo 
        print("Cadastro atualizado com sucesso!\n")

    def vizualizar_cliente(self):
        print(f" ID: {self._id_vendedor}\n Nome Completo: {self._nome_completo}\n Nome de usuário: {self._nome_usuario}\n Data nascimento: {self._data_nasc}\n Login: {self._login}\n Senha: {self._senha}\n Confirma senha: {self._confirma_senha}\n RG: {self._rg}\n CPF: {self._cpf}\n CNH: {self._cnh}\n E-mail: {self._email}\n Telefone: {self._telefone}\n Cidade: {self._cidade}\n Estado: {self._estado}\n CEP: {self._cep}\n Rua: {self._rua}\n N° casa: {self._numero_casa}\n Complemento: {self._complemento}\n")

    def excluir_cliente(self, id_vendedor):
        self._id = id_vendedor
        print("Vendedor excluído.")

    def ativo(self):
        self._ativo = True
    
    def inativo(self):
        self._inativo = False

if __name__ == '__main__':  
    cliente = Cliente()
    cliente.cadastrar_cliente()
    cliente.atualizar_cad_cliente()
    cliente.vizualizar_cliente()
    cliente.excluir_cliente()
    cliente.ativo()
    cliente.inativo()
