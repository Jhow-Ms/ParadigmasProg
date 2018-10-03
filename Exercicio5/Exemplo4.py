class Animal:
    def __init__(self, nome):
        self.nome = nome
        print("Animal sendo construido")

    def quemSouEu(self):
        print("Animal")

    def __str__(self):
        return f'Animal:{self.nome}'

    def __len__(self):
        return len(self.nome)

    def __del__(self):
        print(f'{self.nome} sendo apagado')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog sendo construido")

    def quemSouEu(self):
        print("Dog")

a = Animal("cachorro")

#a.quemSouEu()
#c = Dog()
#c.quemSouEu()