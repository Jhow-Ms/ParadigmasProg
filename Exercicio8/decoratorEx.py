def cria_decorator(funcao):
    def decorator():
        print("Testando")
    return decorator

@cria_decorator
def a_ser_decorada():
    print("Estou sendo decorada")

a_ser_decorada()