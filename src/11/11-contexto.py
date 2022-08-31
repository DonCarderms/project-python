variavel = 'valor'


def imprimir(dado, prefixo):
    print(prefixo, id(dado), dado)


def funcao(*args):
    global variavel
    variavel = 'outra'
    imprimir(variavel,'Na função')
    

imprimir(variavel,'Antes')

funcao(variavel)

imprimir(variavel,'Depois')

