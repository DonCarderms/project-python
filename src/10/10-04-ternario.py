status = input('Status?').upper().strip()

if status not in ['A','I']:
    print('Opção inválida')
    exit(1)

mensagem = 'Ativo' if status == 'A' else 'Inativo'

# Código equivalente
# if status == 'A':
#     mensagem = 'Ativo'
# elif status == 'I':
#     mensagem = 'Inativo'
# else:
#     print('Opção inválida')
#     exit()

print('Status', mensagem)
