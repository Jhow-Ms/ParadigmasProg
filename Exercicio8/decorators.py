def cria_hello_decorator(funcao):
    def hello_decorators():
        print("Antes")
        funcao()
    return hello_decorators()

def hello_decorators():
    print("Hello decorators")

cria_hello_decorator(hello_decorators)