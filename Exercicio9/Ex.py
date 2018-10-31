from functools import partial

def soma (a,b,c):
    return a + b + c
soma1 = partial (soma,1)
soma12 = partial (soma1,2)

print(soma12(3))