# Defina a função prodnlista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prodnlista([1,2,3,4,5,6]) = 720

prodnlista = lambda list: list[len(list) -1] * prodnlista(list[:-1]) if len(list) > 0 else 1

assert (prodnlista([1,2,3,4,5,6]) == 720)
print(prodnlista([1,2,3,4,5,6]))