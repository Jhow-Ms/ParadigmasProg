# Defna a função todosnimparesQ que recebe como argumento uma lista de
# números inteiros w e devolve True se w contém apenas números ímpares e False
# em caso contrário.
# Ex: todosnimparesQ([1,3,5,7]) = True
# Ex: todosnimparesQ([]) = True
# Ex: todosnimparesQ([1,2,3,4,5]) = False


def todos_imparesQ(w):
    return True if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and todos_imparesQ(w[:-1])) else False

print(todos_imparesQ([1,1,3,7,11]))
print(todos_imparesQ([]))
print(todos_imparesQ([2,4,6,8,10]))