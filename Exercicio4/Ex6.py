#6 Espião: Escreva uma função que receba uma lista de inteiros e retorne True se contém um 007 em ordem, mesmo que não contínuo. Exemplo:
#- espiao([1,2,4,0,0,7,5]) --> True
#- espiao([1,0,2,4,0,5,7]) --> True
#- espiao([1,7,2,4,0,5,0]) --> False

def espiao(lista):
    status = "Nada"
    for letra in lista:
        if letra == 0:
            if status == "Nada":
                status = "etapa1"
            elif status == "etapa1":
                status = "etapa2"
        elif letra == 7:
            if status == "etapa2":
                return True
    return False

print(espiao([2,3,0,0,7]))
print(espiao([1,5,6,8,0,7,5,7]))
print(espiao([0,1,5,8,9,0,5,6,7]))