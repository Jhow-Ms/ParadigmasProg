# Defna a função somannat que recebe como argumento um número natural n
# e devolve a soma de todos os números naturais até n.
# Ex: somannat(5) = 15

soma_nat = lambda n: 1 if n == 1 else n + soma_nat(n - 1)
print(soma_nat(2),soma_nat(1),soma_nat(5))