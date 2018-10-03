class Livro:
    def __init__(self):
        self.titulo = titulo
        self.numero_paginas = numero_paginas
        self.aberto = False

    def abrir(self):
        self.aberto = True

    def fechar(self):
        self.aberto = False

l = Livro ("Python como programar",500):
a = 2
b = 2.2
c = "abc"
print(type(l),type(a), type(b), type(c), type(l))