# Defina a função div que recebe como argumentos dois números naturais m
# e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
# inteira.
# Ex: div(7,2) = 3

div = lambda dividendo, divisor: 0 if dividendo < divisor else +1 + div(dividendo - divisor,divisor)
print(div(7,2))
