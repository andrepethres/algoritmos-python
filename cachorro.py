class Cachorro:

    def __init__(self, nome, sono, ano_nascimento, comer):
        self._nome = nome
        self._sono = sono
        self._ano_nascimento = ano_nascimento
        self._comer = comer
        self._comida = 1000

    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

    def get_sono(self):
        return self._sono

    def set_sono(self, sono):
        self._sono = sono

    def get_ano_nascimento(self):
        return self._ano_nascimento
    
    def set_ano_nascimento(self, ano_nascimento):
        self._ano_nascimento = ano_nascimento

    def get_comer(self):
        return self._comer
    
    def set_comer(self, comer):
        self._comer = comer

    def get_comida(self):
        return self._comida
    
    def set_comida(self, comida):
        self._comida = comida
    

    def imprimir_informacoes(self):
        print(f" Nome: {self._nome}\n Sono: {self._sono}\n Ano Nascimento: {self._ano_nascimento}\n Comida: {"%0.1f" % self._comida}")

    def latir(self):
        print(f"{self._nome} diz: 'AU AU AU AU AU' ({str(self._nome).upper()})")
    
    def comer(self):
        self.set_comida(self.get_comida() - 0.1)
        self.imprimir_informacoes()

    # print(cachorro_freddy.get_nome())
    # print(cachorro_freddy.get_comida())
    # print(cachorro_freddy.get_comer())
    # print(cachorro_freddy.get_ano_nascimento())
    # print(cachorro_freddy.get_sono())

    # cachorro_freddy.imprimir_informacoes()
    # cachorro_freddy.ano_nascimento = 2019
    # cachorro_freddy.sono = True
    # cachorro_freddy.imprimir_informacoes() 

print("---------------------------------------------------")

if __name__ == '__main__':
    cachorro_pitoco = Cachorro("Pitoco",0.5, 2022, True)
    cachorro_pitoco.latir()
    cachorro_pitoco.set_nome("Pitocolino")
    cachorro_pitoco.set_comida(1.0)
    cachorro_pitoco.set_ano_nascimento("2024")
    cachorro_pitoco.set_sono("False")
    cachorro_pitoco.imprimir_informacoes()

    
    # print(cachorro_pitoco.get_nome())
    # print(cachorro_pitoco.get_comida())
    # print(cachorro_pitoco.get_ano_nascimento())
    # print(cachorro_pitoco.get_sono())

    # cachorro_pitoco.imprimir_informacoes()
    # cachorro_pitoco.ano_nascimento = 2023
    # cachorro_pitoco.sono = False
    # cachorro_pitoco.imprimir_informacoes()
   