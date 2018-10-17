import time
def cria_decorator_que_mede_tempo(funcao):
    def decoradora():
        t0 = time.time()
        print(f'------(funcao.__name__)-----')
        funcao()
        return time.time() - t0
    return decoradora()
def funcao_rapidinho():
    for i in range(10):
        print(i)

def funcao_demorada():
    for i in range(10):
        print(i)
        time.sleep(1)
funcao_rapidinho = cria_decorator_que_mede_tempo(funcao_rapidinho)
funcao_demorada = cria_decorator_que_mede_tempo(funcao_demorada)

funcao_rapidinho()
funcao_demorada()