class Carro:

    def __init__(self, id_carro="", marca="", modelo="", placa="", cor="", ano_fab="", ano_mod="", potencia="", tipo="", km="", renavam="", ipva="", origem="", combustivel="", preco_compra="", preco_venda="", cidade_uf="", portas="", qnt_lugares="", ar_cond="", trava_vidros="", direcao="", manual="", chave_reserva="", step="", triangulo="", macaco="", chave_roda="", status="", data_entrada="", data_saida="", mecanica="", lavacao="", fipe="", n_chassi="", ativo="", inativo=""):
        self._id_carro = id_carro
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._cor = cor
        self._ano_fab = ano_fab
        self._ano_mod = ano_mod
        self._potencia = potencia
        self._tipo = tipo
        self._km = km
        self._renavam = renavam
        self._ipva = ipva
        self._origem = origem
        self._combustivel = combustivel
        self._preco_compra = preco_compra
        self._preco_venda = preco_venda
        self._cidade_uf = cidade_uf
        self._portas = portas
        self.qnt_lugares = qnt_lugares
        self._ar_cond = ar_cond
        self._trava_vidros = trava_vidros
        self._direcao = direcao
        self._manual = manual
        self._chave_reserva = chave_reserva
        self._step = step
        self._triangulo = triangulo
        self._macaco = macaco
        self._chave_roda = chave_roda
        self._status = status
        self._data_entrada = data_entrada
        self._data_saida = data_saida
        self._mecanica = mecanica
        self._lavacao = lavacao
        self._fipe = fipe
        self.n_chassi = n_chassi
        self._ativo = ativo
        self._inativo = inativo

    def get_id_carro(self):
        return self._id_carro
    
    def set_id_carro(self, id_carro):
        self._id_carro = id_carro

    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_placa(self):
        return self._placa
    
    def set_placa(self, placa):
        self._placa = placa

    def get_cor(self):
        return self._cor
    
    def set_senha(self, cor):
        self._cor = cor

    def get_ano_fab(self):
        return self._ano_fab
    
    def set_ano_fab(self, ano_fab):
        self._ano_fab = ano_fab

    def get_ano_mod(self):
        return self._ano_mod
    
    def set_ano_mod(self, ano_mod):
        self._ano_mod = ano_mod
    
    def get_potencia(self):
        return self._potencia
    
    def set_potencia(self, potencia):
        self._potencia = potencia

    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_km(self):
        return self._km
    
    def set_km(self, km):
        self._km = km

    def get_renavam(self):
        return self._renavam
    
    def set_renavam(self, renavam):
        self._renavam = renavam

    def get_ipva(self):
        return self._ipva
    
    def set_ipva(self, ipva):
        self._ipva = ipva

    def get_origem(self):
        return self._origem
    
    def set_origem(self, origem):
        self._origem = origem

    def get_combustivel(self):
        return self._combustivel
    
    def set_combustivel(self, combustivel):
        self._combustivel = combustivel

    def get_preco_compra(self):
        return self._preco_compra
    
    def set_preco_compra(self, preco_compra):
        self._preco_compra = preco_compra

    def get_preco_venda(self):
        return self._preco_venda
    
    def set_preco_venda(self, preco_venda):
        self._preco_venda = preco_venda

    def get_cidade_uf(self):
        return self._cidade_uf
    
    def set_cidade_uf(self, cidade_uf):
        self._cidade_uf = cidade_uf

    def get_portas(self):
        return self._portas
    
    def set_portas(self, portas):
        self._portas = portas

    def get_qnt_lugares(self):
        return self._qnt_lugares
    
    def set_qnt_lugares(self, qnt_lugares):
        self._qnt_lugares = qnt_lugares

    def get_ar_cond(self):
        return self._ar_cond
    
    def set_ar_cond(self, ar_cond):
        self._ar_cond = ar_cond

    def get_trava_vidros(self):
        return self._trava_vidros
    
    def set_trava_vidros(self, trava_vidros):
        self._trava_vidros = trava_vidros

    def get_direcao(self):
        return self._direcao
    
    def set_direcao(self, direcao):
        self._direcao = direcao

    def get_manual(self):
        return self._manual
    
    def set_manual(self, manual):
        self._manual = manual

    def get_chave_reserva(self):
        return self._chave_reserva
    
    def set_chave_reserva(self, chave_reserva):
        self._chave_reserva = chave_reserva

    def get_step(self):
        return self._step
    
    def set_step(self, step):
        self._step = step

    def get_triangulo(self):
        return self._triangulo
    
    def set_triangulo(self, triangulo):
        self._triangulo = triangulo

    def get_macaco(self):
        return self._macaco
    
    def set_macaco(self, macaco):
        self._macaco = macaco

    def get_chave_roda(self):
        return self._chave_roda
    
    def set_chave_roda(self, chave_roda):
        self._chave_roda = chave_roda

    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._staus = status

    def get_data_entrada(self):
        return self._data_entrada
    
    def set_data_entrada(self, data_entrada):
        self._data_entrada = data_entrada

    def get_data_saida(self):
        return self._data_saida
    
    def set_data_saida(self, data_saida):
        self._data_saida = data_saida

    def get_mecanica(self):
        return self._mecanica
    
    def set_mecanica(self, mecanica):
        self._mecanica = mecanica

    def get_lavacao(self):
        return self._lavacao
    
    def set_lavacao(self, lavacao):
        self._lavacao = lavacao

    def get_fipe(self):
        return self._fipe
    
    def set_fipe(self, fipe):
        self._fipe = fipe

    def get_n_chassi(self):
        return self.n_chassi
    
    def set_n_chassi(self, n_chassi):
        self._fipe = n_chassi

    def get_ativo(self):
        return self._ativo
    
    def set_ativo(self, ativo):
        self._ativo = ativo

    def get_inativo(self):
        return self._inativo
    
    def set_inativo(self, inativo):
        self._inativo = inativo

    def cadastrar_carro(self):
        print(">>>CADASTRE-SE<<<\n")
        print("|DADOS DO VEÍCULO|\n")
        self._id_carro = input("ID carro:")
        self._marca = input("Digite a marca do carro:")
        self._modelo = input("Digite o modelo:")
        self._placa = input("Placa:")
        self._cor = input("Cor:")
        self._ano_fab = input("Ano fabricação:")
        self._ano_mod = input("Ano modelo:")
        self._potencia = input("Potência:")
        self._tipo = input("Tipo(Novo, semi-novo ou usado):")
        self._km = input("Km:")
        self._renavam = input("N° renavam:")
        self._combustivel = input("Combustível:")
        self._preco_compra = input("Preço compra:")
        self._preco_venda = input("Preço venda:")
        self._cidade_uf = input("Cidade/Estado:")
        self._portas = input("Portas:")
        self._qnt_lugares = input("Lugares:")
        self._ar_cond = input("Ar condicionado(s/n):")
        self._trava_vidros = input("Trava-vidros(s/n):")
        self._direcao = input("Direção:")
        self._manual = input("Manual(s/n):")
        self._chave_reserva = input("Chave reserva(s/n):")
        self._step = input("Step(s/n):")
        self._triangulo = input("Triângulo(s/n):")
        self._macaco = input("Macaco(s/n):")
        self._chave_roda = input("Chave de roda(s/n):")
        self._status = input("Disponível?(s/n):")
        self._data_entrada = input("Data entrada:")
        self._data_saida = input("Data saída:")
        self._mecanica = input("Está na mecânica?(s/n):")
        self._lavacao = input("Está na lavação?(s/n):")
        self._fipe = input("Fipe:")
        self._n_chassi = input("N° chassi:")
        self._ativo 
        self._inativo 
        print("Carro cadastrado com sucesso!\n")

    def atualizar_cad_carro(self):
        print(">>>CADASTRE-SE<<<\n")
        print("|DADOS DO VEÍCULO|\n")
        self._id_carro = input("ID carro:")
        self._marca = input("Digite a marca do carro:")
        self._modelo = input("Digite o modelo:")
        self._placa = input("Placa:")
        self._cor = input("Cor:")
        self._ano_fab = input("Ano fabricação:")
        self._ano_mod = input("Ano modelo:")
        self._potencia = input("Potência:")
        self._tipo = input("Tipo:")
        self._km = input("Km:")
        self._renavam = input("N° renavam:")
        self._combustivel = input("Combustível:")
        self._preco_compra = input("Preço compra:")
        self._preco_venda = input("Preço venda:")
        self._cidade_uf = input("Cidade/Estado:")
        self._portas = input("Portas:")
        self._qnt_lugares = input("Lugares:")
        self._ar_cond = input("Ar condicionado(s/n):")
        self._trava_vidros = input("Trava-vidros(s/n):")
        self._direcao = input("Direção:")
        self._manual = input("Manual(s/n):")
        self._chave_reserva = input("Chave reserva(s/n):")
        self._step = input("Step(s/n):")
        self._triangulo = input("Triângulo(s/n):")
        self._macaco = input("Macaco(s/n):")
        self._chave_roda = input("Chave de roda(s/n):")
        self._status = input("Status:")
        self._data_entrada = input("Data entrada:")
        self._data_saida = input("Data saída:")
        self._mecanica = input("Está na mecânica?(s/n):")
        self._lavacao = input("Está na lavação?(s/n):")
        self._fipe = input("Fipe:")
        self._n_chassi = input("N° chassi:")
        self._ativo 
        self._inativo 
        print("Cadastrado carro atualizado com sucesso!\n")

    def vizualizar_carro(self):
        print(f" ID carro: {self._id_carro}\n Digite a marca do carro: {self._marca}\n Modelo: {self._modelo}\n Placa: {self._placa}\n Cor: {self._cor}\n Ano fabricação: {self._ano_fab}\n Ano modelo: {self._ano_mod}\n Potência: {self._potencia}\n Tipo: {self._tipo}\n Km: {self._km}\n N° Renavam: {self._renavam}\n Origem: {self._origem}\n Combustível: {self._combustivel}\n Preço compra: {self._preco_compra}\n Preço venda: {self._preco_venda}\n Cidade/Estado: {self._cidade_uf}\n Portas: {self._portas}\n Lugares: {self._qnt_lugares}\n Ar condicionado: {self._ar_cond}\n Trava vidros: {self._trava_vidros}\n Direção: {self._direcao}\n Manual(s/n): {self._manual}\n Chave reserva(s/n): {self._chave_reserva}\n Step(s/n): {self._step}\n Triângulo(s/n): {self._triangulo}\n Macaco(s/n): {self._macaco}\n Chave de roda(s/n): {self._chave_roda}\n Status: {self._status}\n Data entrada: {self._data_entrada}\n Data saída: {self._data_saida}\n Está na mecânica?(s/n): {self._mecanica}\n Está na lavação?(s/n): {self._lavacao}\n Fipe: {self._fipe}\n N° chassi: {self._n_chassi}\n")

    def excluir_carro(self, id_carro):
        self._id_carro = id_carro
        print("Carro excluído.")

    def ativo(self):
        self._ativo = True
    
    def inativo(self):
        self._inativo = False

if __name__ == '__main__':  
    carro = Carro()
    carro.cadastrar_carro()
    carro.atualizar_cad_carro()
    carro.vizualizar_carro()
    carro.excluir_carro()
    carro.ativo()
    carro.inativo()