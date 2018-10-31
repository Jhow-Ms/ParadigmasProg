from functools import partial
def eq2grau(a, b, c, x):
    return a * x ** 2 +b * x +c
#eq2grau1 = partial(eq2grau,1)
#eq2grau11 = partial(eq2grau1,1)
#eq2grau111 = partial(eq2grau11,1)
eq2grau111 = print(partial(partial(eq2grau,1),1),1)
print(eq2grau111(5))