
def processo(valor):
    print(id(valor), valor)
    valor = valor + 1
    print(id(valor), valor)
    print('---')


valor = 10
print(id(valor), valor)
processo(valor)
print(id(valor), valor)


# lista = [1, 2, 3, 4, 5]
# lista2 = lista
# lista3 = lista.copy()
# print('Lista', lista, id(lista))
# print('Lista2', lista2, id(lista2))
# print('Lista3', lista3, id(lista3))

# lista2[1] = 10
# print('Lista', lista, id(lista))
# print('Lista2', lista2, id(lista2))
# print('Lista3', lista3, id(lista3))
