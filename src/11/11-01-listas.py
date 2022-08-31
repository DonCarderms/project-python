# perguntar ao usuário, um número entre 1 e 10 inclusive
#  e armazenar numa variável

n = int(input('Número de items: '))

# Criar uma lista de números em sequencia
# com tamanho igual ao número anterior

lista = list(range(1, n+1))

# Exibir a lista
print(lista)
# Criar uma nova lista, apenas com os números pares

lista_pares = [numero
               for numero in lista
               if numero % 2 == 0]

# Exibir a nova lista
print(lista_pares)

lista_multiplos_3 = [numero
                     for numero in lista
                     if numero % 3 == 0]
print(lista_multiplos_3)
