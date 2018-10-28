# Escreva uma função que exibe uma lista recebida como parâmetro. Ela deve,
# contudo, ordenar a lista antes. A ordenação deve ser feita por meio de um
# decorator.

def ordena(f):
	def decorator(lista):
		return f(sorted(lista))
	return decorator

@ordena
def funcao(lista):
	print(lista)
print(funcao([7,3,6,2,0,1,4,5]))