# Herança simples e hierárquica

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} fazer um som.")

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} late.")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia.")

if __name__ == "__main__":
    cachorro = Cachorro("Rex")
    gato = Gato ("Mimi")
    cachorro.fazer_som()
    gato.fazer_som()

# Herança múltipla

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz qua qua qua.")

class Voar:
    def pode_voar(self):
        print("Este animal pode voar.")

class Pato(Animal, Voar):
    def _init__(self, nome):
        Pato. __init__(self, nome) # Inicializa a classe base Animal

    def nadar(self):
        print(f"{self.nome} está nadando!")

    def bota_ovo(self):
        print(f"{self.nome} bota ovo.")

if __name__ == "__main__":
    pato = Pato("Donald") 
    pato.falar()        # Método da classe Animal
    pato.pode_voar()    # Método da classe Voar
    pato.nadar()        # Método da classe Nadar
    pato.bota_ovo()     # Método da classe Bota ovo

# Herança múltipla

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def faz_som(self):
        print(f"{self.nome} faz po pó.")

class Voar:
    def pode_voar(self):
        print("Este animal pode voar.")

class Galinha(Animal, Voar):
    def _init__(self, nome):
        Animal. __init__(self, nome) # Inicializa a classe base Animal

    def comer(self):
        print(f"{self.nome} está comendo milho!")

    def bota_ovo(self):
        print(f"{self.nome} bota ovo.")

if __name__ == "__main__":
    galinha = Galinha("Pintadinha") 
    galinha.faz_som()      # Método da classe Animal
    galinha.pode_voar()    # Método da classe Voar
    galinha.comer()        # Método da classe Comer
    galinha.bota_ovo()     # Método da classe Bota ovo

# Herança múltipla

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som.")

class Ornitorrinco(Animal, Voar):
    def _init__(self, nome):
        Animal. __init__(self, nome) # Inicializa a classe base Animal

    def nadar(self):
        print(f"{self.nome} está nadando!")

    def bota_ovo(self):
        print(f"{self.nome} bota ovo.")

if __name__ == "__main__":
    ornitorrinco = Ornitorrinco("Bicudo") 
    ornitorrinco.falar()        # Método da classe Animal
    ornitorrinco.nadar()        # Método da classe Nadar
    ornitorrinco.bota_ovo()     # Método da classe Bota ovo

# Herança múltipla

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som.")

class Voar:
    def comer(self):
        print("Este animal pode voar.")

class Panda(Animal, Voar):
    def _init__(self, nome):
        Animal. __init__(self, nome) # Inicializa a classe base Animal

    def nadar(self):
        print(f"{self.nome} está nadando!")

    def comer(self):
        print(f"{self.nome} está comendo bambu!")

if __name__ == "__main__":
    panda = Panda("Panda") 
    panda.falar()        # Método da classe Animal
    panda.nadar()        # Método da classe Nadar
    panda.comer()        # Método da classe Comer