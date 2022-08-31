# Calculo imposto renda
# Tabela
# < 1000 = isento
# < 2000 = 2.5%
# < 5000 = 5%
# < 10000 = 10%
# >= 10000 = 15%

def valor_ir(salario):
    if salario <= 0:
        raise ValueError('Salário deve ser positivo')
    elif salario < 1000:
        ali = 0
    elif salario < 2000:
        ali = 2.5
    elif salario < 5000:
        ali = 5
    elif salario < 10000:
        ali = 10
    else:
        ali = 15

    return ali, salario * ali / 100


for salario in [500, 1025, 3000, 5300, 100000]:
    print(salario, valor_ir(salario))
