from functools import partial
from inspect import signature
def curry(f):
    def aux(x):
        if len(signature(f).parameters) == 1:
            return f(x)
        return curry(partial(f, x))
    return aux
@curry
def funcao (x,y):
    return x + y ** 2
funcao_2 = funcao(2)
print(funcao (2)(3),funcao_2(3))
#print(funcao_2(5))