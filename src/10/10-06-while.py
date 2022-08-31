continuar = True

while continuar:
    nome = input('Nome?').strip()
    if not nome:
        print('Você deve informar seu nome')
        continue
    if len(nome) < 2:
        print('Você deve ter um nome com mais de 1 caracter')
        continue
    continuar = False

print('Seu nome', nome)
