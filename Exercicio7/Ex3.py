# 3 Defina a função primnalg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais signifcatvo) na representação decimal de n.
# Ex: primnalg(5649) = 5
# Ex: primnalg(7) = 7

primnalg = lambda n: n if n < 10 else primnalg(n//10)
print(primnalg(5649))
print(primnalg(7))