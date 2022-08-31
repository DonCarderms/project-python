# Criar um dicionário aninhado
dicionario = {
    'pt': {
        'casa': 'CASA',
        'cão': 'CACHORRO'
    },
    'en': {
        'casa': 'HOUSE',
        'cão': 'DOG'
    }
}

# Função que imprime o valor de uma chave no dicionário
def traduzir(lingua, palavra):
    print(dicionario[lingua][palavra])


traduzir('en', 'cão')
