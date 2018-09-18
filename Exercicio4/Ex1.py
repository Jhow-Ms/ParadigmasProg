#1 Menor de dois pares: Escreva uma função que retorne o menor de dois números dados se ambos os números forem pares, mas retorna o maior se um dos dois for ímpar. Exemplo:
#- menor_de_dois_pares(2,4) --> 2
#- menor_de_dois_pares (2,5) --> 5

def menor_de_dois_pares(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        return a
    else:
        if a > b:
            return a
        return b


print(menor_de_dois_pares(2, 4))
print(menor_de_dois_pares(2, 5))