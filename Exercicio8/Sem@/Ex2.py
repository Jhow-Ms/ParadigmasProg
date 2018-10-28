# Escreva uma função que recebe uma lista de triplas e, para cada uma, gera uma
# equação do segundo grau considerando que os elementos da tripla são os
# coeficientes usualmente denominados a, b e c da equação. Note que a sua função
# deverá devolver uma lista de equações. A geração das equações deve ser feita por
# meio de, evidentemente, decorators.

def recebe(f):
	equacoes = []
	def decorator(lista):
		for e in lista:
			equacoes.append(f(e))
		return equacoes
	return decorator
def funcao(lista):
	equacao = str(lista) + "xˆ2" + "+" + str(lista) + "x" + "+"+ str(lista)
	return equacao
funcao = recebe(funcao)
print(funcao([2,4,5]))