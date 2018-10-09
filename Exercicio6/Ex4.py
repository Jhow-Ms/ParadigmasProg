# Defna a função prodnlista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prodnlista([1,2,3,4,5,6]) = 720

def prodnlista(a,i):
    return a[i] if i == 0 else a[i] * prodnlista(a[:-1],i-1)
print(prodnlista([1,2,3,4,5,6],5))