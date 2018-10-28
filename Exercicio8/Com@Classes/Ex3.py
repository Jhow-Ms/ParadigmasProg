# Escreva uma função que exibe uma lista recebida como parâmetro. Ela deve,
# contudo, ordenar a lista antes. A ordenação deve ser feita por meio de um
# decorator.

class ordena:
    def __init__(self, f):
        self.f = f
    def __call__(self, lista):
        return self.f(sorted(lista))
@ordena
def funcao(lista):
    print(lista)
print(funcao([7,3,6,2,0,1,4,5]))