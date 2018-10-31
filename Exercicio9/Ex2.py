from functools import partial
from inspect import signature
def curry (f):
    def aux(x):
        if len(signature(f).parameters) == 1:
            return f(x)
        return curry(partial(f,x))
    return aux
@curry
def soma(a, b, c):
    return a + b + c
print(soma(1)(2)(3))
