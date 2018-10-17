# Defina a função pertence que recebe como argumentos uma lista de números
# inteiros o e um número inteiro n e devolve True se n ocorre em o e False em
# caso contrário.
# Ex: pertence ([1,2,3],1) = True
# Ex: pertence ([1,2,3],2) = True
# Ex: pertence ([1,2,3],3) = True
# Ex: pertence ([1,2,3],4) = False


pertence = lambda list,n: True if n in list else False

print(pertence([1,2,3],1))
print(pertence([1,2,3],2))
print(pertence([1,2,3],3))
print(pertence([1,2,3],4))
print(pertence([1,2,3],5))