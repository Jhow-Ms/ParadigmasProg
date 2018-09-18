#4 - Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros,
#  houver em alguma posição da lista um 3 do lado de outro 3.
#  Exemplo:

def tem_33(lista):
    status = "Nada"
    for simbolo in lista:
        if simbolo == 3:
            if status == "Nada":
                status = "Tres"
            elif status == "Tres":
                return True
            else:
                if status == "Tres":
                    status = "Nada"
        return False


print(tem_33([3, 3, 1]))
print(tem_33([3, 1, 3, 1, 3, 1]))
print(tem_33([1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 3]))     