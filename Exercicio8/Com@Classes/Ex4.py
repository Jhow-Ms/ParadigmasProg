# Escreva uma classe para representar um café que, a princípio, tem somente preço.
# Um cafezinho custa 5 reais. Escreva classes para representar os adicionais: palitos de
# chocolate (0,50 cents), espuma de leite (0,20 cents), caramelo (0,10 cents) e canela
# (0,30 cents). Crie um objeto café e, a seguir, faça um menuzinho em que o usuário
# pode fcar indefnidamente escolhendo adicionais: 1 para chocolate, 2 para espuma
# de leite, 3 para caramelo e 4 para canela. A cada adicional escolhido, decore o objeto
# café. No fnal, mostre o preço total.

class Cafe:
    def __init__(self, preco = 5.0):
        self.preco = preco

    def __call__(self, adicional):
        self.preco += adicional.preco
        return self.preco


class Palitos_de_chocolate:
    def __init__(self, palitos_chocolate = 0.5):
        self.preco = palitos_chocolate


class Espuma_de_leite:
    def __init__(self, espuma_de_leite = 0.2):
        self.preco = espuma_de_leite


class Caramelo:
    def __init__(self, caramelo = 0.1):
        self.preco = caramelo

class Canela:
    def __init__(self, canela = 0.3):
        self.preco = canela

def opcoes():
    return int(
                input("1 - Adicionar Palitos de chocolate \n" + "2 - Adicionar Espuma de leite \n" +"3 - Adicionar Caramelo \n" +"4 - Adicionar Canela \n" +"0 - Sair \n"
                )
            )

tipo = opcoes()
cafe = Cafe
while (tipo != 0):
    if tipo == 1:
        print("Palitos de chocolate no seu café")
        cafe(Palitos_de_chocolate())
    if tipo == 2:
        print("Espuma de leite no seu café!")
        cafe(Espuma_de_leite())
    if tipo == 3:
        print("Caramelo no seu café!")
        cafe(Caramelo())
    if tipo == 4:
        print("Canela no seu café!")
        cafe(Canela())
    tipo = opcoes()
print("Valor Total:",cafe.preco)