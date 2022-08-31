try:
    x = float(input('Numero 1: '))
    y = float(input('Numero 2: '))
    print(f'{x:.2f}+{y:.2f}={x+y:.2f}')
    print(f'{x}-{y}={x-y}')
    print(f'{x}*{y}={x*y}')
    print(f'{x}/{y}={x/y}')

    print(f'{x}%{y}={x%y}')
    print(f'{x}//{y}={x//y}')
    print(f'{x}**{y}={x**y}')

except ZeroDivisionError:
    print("Não dá pra dividir por zero!")
# except ValueError:
#     print("O número deve ser válido!")
except Exception as exc:
    print('Erro geral', exc)