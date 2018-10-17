# Defina a função junta que recebe como argumentos duas listas de números
# inteiros o1 e o2 e devolve a concatenação de o1 com o2 .
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]

junta = lambda x, y: x + y if len(x) > 0 and len(y) > 0 else []

print(junta([1,2,3], [4,5,6]))
print(junta([5,6,7],[8,9,10]))
print(junta([5,6],[7,9]))