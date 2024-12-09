# Herança múltipla

class Veiculo:
    def __init__(self, nome):
        self.nome = nome
class Andar:
    def andar(self):
        print(f"Estou andando de {self.nome}.")
class Acelerar:
    def pedalar(self):
        print("Pedalando rápido.")
class Grau:
    def dar_grau(self):
        print("Estou dando grau!")
class Frear:
    def frear(self):
        print("Freei.")
class DiminuirVelocidade:
    def diminuir_velocidade(self):
        print("Diminui a velocidade.")
class Dirigir:
    def dirigir(self):
        print(f"Estou dirigindo meu {self.nome}.")
class Acelerar_veiculo:
    def acelerar_veiculo(self):
        print(f"Acelerando...")
class Embarcar:
    def embarcar(self):
        print(f"Embarquei.")
class Desembarcar:
    def desembarcar(self):
        print(f"Desembarquei.")
class Carregar_produto:
    def carregar(self):
        print(f"Carregar produto no {self.nome}.")
class Percurso:
    def percurso(self):
        print(f"Percorrendo percurso.")
class Descarregar_produto:
    def descarregar(self):
        print(f"Descarregando produto no destino.")
class Nome_veiculo:
    def nome_veiculo(self):
        print(f">>>{self.nome}<<<")

class Bicicleta(Veiculo, Nome_veiculo, Embarcar, Andar, Acelerar, Grau, Frear, DiminuirVelocidade, Desembarcar):
    def _init__(self, nome):
        Veiculo. __init__(self, nome) # Inicializa a classe base Veículo

class Moto(Veiculo, Nome_veiculo, Embarcar, Andar, Acelerar_veiculo, Grau, DiminuirVelocidade, Frear, Desembarcar ):
    def _init__(self, nome):
        Veiculo. __init__(self, nome) # Inicializa a classe base Veículo

class Carro(Veiculo, Nome_veiculo, Embarcar, Dirigir, Acelerar_veiculo, Frear, DiminuirVelocidade, Desembarcar):
    def _init__(self, nome):
        Veiculo. __init__(self, nome) # Inicializa a classe base Veículo
class Caminhao(Veiculo, Nome_veiculo, Embarcar, Dirigir, Acelerar_veiculo, DiminuirVelocidade, Frear, Carregar_produto, Percurso, Descarregar_produto):
    def _init__(self, nome):
        Veiculo. __init__(self, nome) # Inicializa a classe base Veículo

if __name__ == "__main__":
    bicicleta = Bicicleta("Bicicleta") 
    bicicleta.nome_veiculo()        # Imprimir nome do veículo
    bicicleta.embarcar()            # Método da classe Embarcar
    bicicleta.pedalar()             # Método da classe Pedalar
    bicicleta.dar_grau()            # Método da classe Grau
    bicicleta.frear()               # Método da classe Frear
    bicicleta.diminuir_velocidade() # Método da classe Diminuir Velocidade
    moto = Moto("Moto")
    moto.nome_veiculo()          # Imprimir nome do veículo
    moto.embarcar()              # Método da classe Embarcar
    moto.andar()                 # Método da classe Andar
    moto.acelerar_veiculo()      # Método da classe Acelerar
    moto.dar_grau()              # Método da classe Grau
    moto.diminuir_velocidade()   # Método da classe Diminuir Velocidade
    moto.frear()                 # Método da classe Frear
    moto.desembarcar()           # Método da classe Desembarcar
    carro = Carro("Carro")
    carro.nome_veiculo()        # Imprimir nome do veículo
    carro.embarcar()            # Método da classe Embarcar
    carro.dirigir()             # Método da classe Dirigir
    carro.acelerar_veiculo()    # Método da classe Acelerar veículo
    carro.diminuir_velocidade() # Método da classe Diminuir Velocidade
    carro.frear()               # Método da classe Frear
    carro.desembarcar()         # Método da classe Desembarcar
    caminhao = Caminhao("Caminhão")
    caminhao.nome_veiculo()        # Imprimir nome do veículo
    caminhao.embarcar()            # Método da classe Embarcar
    caminhao.dirigir()             # Método da classe Dirigir
    caminhao.acelerar_veiculo()    # Método da classe Acelerar
    caminhao.diminuir_velocidade() # Método da classe Diminuir Velocidade
    caminhao.frear()               # Método da classe Frear
    caminhao.carregar()            # Método da classe Carregar Produto
    caminhao.percurso()            # Método da classe Percurso
    caminhao.descarregar()         # Método da classe Descarregar 