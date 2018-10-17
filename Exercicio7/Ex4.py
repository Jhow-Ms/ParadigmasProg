# Defina a função prodnlista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prodnlista([1,2,3,4,5,6]) = 720

prodnlista = lambda a,i:0 if i == 0 else a * prodnlista(a -1, i-1)
print(prodnlista([1,2,3,4,5,6]))