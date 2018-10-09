# Defna a função contemnparQ que recebe como argumento uma lista de números
# inteiros w e devolve True se w contém um número par e False em caso contrário.
# Ex: contemnparQ([2,3,1,2,3,4]) = True
# Ex: contemnparQ([1,3,5,7]) = False


def contemparQ(a,i):
    if i == len(a):
        return False
    return True if a[i] % 2 == 0 else contemparQ(a,i+1)

print(contemparQ([2,3,1,2,3,4],0))
print(contemparQ([1,3,5,7],0))