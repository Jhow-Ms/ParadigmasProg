# Escreva uma função que calcula a soma dos n primeiros números naturais, dado
# que n é recebido como parâmetro. Escreva um decorator que garanta que o valor
# recebido é natural (maior ou igual a 1).
class Validar:
	def __init__(self,f):
		self.f = f
	def __call__(self,n):
		if (n>=1):
			return self.f(n)
		else:
			print("Número menor que 1")
			return 0
@Validar
def outra_funcao(n):
	soma=0
	for x in range(n+1):
		soma = soma + x
	return soma

print(outra_funcao(10))
print(outra_funcao(0))
