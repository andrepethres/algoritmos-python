# Class Herança multinível

class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def embarcar(self):
        print(f"Embarquei no meu {self.nome}.")

class Carro(Veiculo):
    def __init__(self, nome, modelo_do_carro):
        super().__init__(nome) # Chama o construtor da classe base (Veiculo)
        self.tipo_do_carro = modelo_do_carro

    def arrancar(self):
        print(f"Estou arrancando.")

class Fusca(Carro):
    def __init__(self, nome, modelo_do_carro, marca):
        super().__init__(nome, modelo_do_carro) # Chama o construtor da classe Fusca
        self.tipo = marca

    def acelerar(self):
        print(f"Cheguei a 100 km/h.")

if __name__ == "__main__":
    carro = Fusca("fuscão preto", "Fusca", "VolksWagen")
    carro.embarcar()    # Método da classe Veiculo
    carro.arrancar()    # Método da classe Arrancar
    carro.acelerar()    # Método da classe Acelerar