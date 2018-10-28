# Escreva uma classe para representar um café que, a princípio, tem somente preço.
# Um cafezinho custa 5 reais. Escreva classes para representar os adicionais: palitos de
# chocolate (0,50 cents), espuma de leite (0,20 cents), caramelo (0,10 cents) e canela
# (0,30 cents). Crie um objeto café e, a seguir, faça um menuzinho em que o usuário
# pode fcar indefnidamente escolhendo adicionais: 1 para chocolate, 2 para espuma
# de leite, 3 para caramelo e 4 para canela. A cada adicional escolhido, decore o objeto
# café. No final, mostre o preço total.

def palitos_de_chocolate(f):
    def decorator():
        return f() + 0.5
    return decorator

def espuma_de_leite(f):
    def decorator():
        return f() + 0.2
    return decorator

def caramelo(f):
    def decorator():
        return f() + 0.1
    return decorator

def canela(f):
    def decorator():
        return f() + 0.3
def cafe():
    return 5.0
def opcoes():
    return int(
                input("1 - Adicionar Palitos de chocolate \n" + "2 - Adicionar Espuma de leite \n" +"3 - Adicionar Caramelo \n" +"4 - Adicionar Canela \n" +"0 - Sair \n"
                )
            )

tipo = opcoes()
while (tipo != 0):
    if tipo == 1:
        print("Palitos de chocolate no seu café")
        cafe = palitos_de_chocolate(cafe)
    if tipo == 2:
        print("Espuma de leite no seu café!")
        cafe = espuma_de_leite(cafe)
    if tipo == 3:
        print("Caramelo no seu café!")
        cafe = caramelo(cafe)
    if tipo == 4:
        print("Canela no seu café!")
        cafe = canela(cafe)
    tipo = opcoes()
print("Valor Total:", cafe())