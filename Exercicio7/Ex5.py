# Defina a função contemnpar que recebe como argumento uma lista de números
# inteiros o e devolve True se o contém um número par e False em caso contrário.
# Ex: contemnpar ([2,3,1,2,3,4]) = True
# Ex: contemnpar ([1,3,5,7]) = False

contemnpar = lambda list: False if len(list) == 0 or (list[len(list)-1]) % 2 != 0 and not contemnpar(list[:-1]) else True

print(contemnpar([2,3,1,2,3,4]))
print(contemnpar([1,3,5,7]))