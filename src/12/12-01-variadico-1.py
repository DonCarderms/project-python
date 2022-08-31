def soma(*valores):
    """
    Valores vai receber todos os argumentos que forem informados,
    independentemente da quantidade.
    A função vai iterar por todos os valores e somar, retornando o resultado
    """
    total = 0
    for valor in valores:
        total += valor

    return total


valor_total = soma(1, 2, 3, 4, 5)
print(valor_total)

valor_total2 = soma(10, 20, 30)
print(valor_total2)
