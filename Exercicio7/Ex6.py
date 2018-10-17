# Defina a função todosnimpares que recebe como argumento uma lista de
# números inteiros o e devolve True se o contém apenas números ímpares e False
# em caso contrário.
# Ex: todosnimpares ([1,3,5,7]) = True
# Ex: todosnimpares ([]) = True
# Ex: todosnimpares ([1,2,3,4,5]) = False


todosnimpares = lambda list: True if len(list) == 0 or (list[len(list) -1]) % 2 != 0 and todosnimpares(list[:-1]) else False

print(todosnimpares([1,3,5,7]))
print(todosnimpares([]))
print(todosnimpares([1,2,3,4,5]))