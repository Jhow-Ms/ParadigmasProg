#3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as palavras na ordem reversa. Exemplo:
#- mestre_yoda('Eu estou em casa') --> 'casa em estou Eu'
#- mestre_yoda('Estamos prontos') --> 'prontos Estamos'


def mestre_yoda(frase):
    lista = frase.split(" ")
    lista.reverse()
    fraseReformulada = "";
    for palavra in lista:
        fraseReformulada = fraseReformulada + palavra + " "
    return fraseReformulada
print(mestre_yoda('Eu estou em casa'))
print(mestre_yoda('Estamos prontos'))