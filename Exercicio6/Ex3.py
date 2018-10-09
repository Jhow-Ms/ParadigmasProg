# 3 Defna a função primnalg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais signifcatvo) na representação decimal de n.
# Ex: primnalg(5649) = 5
# Ex: primnalg(7) = 7

def primalgo(x):
    return x if x < 10 else primalgo(x//10)

print(primalgo(5649))
print(primalgo(7))