import csv

# Abrimos o arquivo em contexto (with/as), assim ele será fechado automaticamente após o término do bloco
with open('exemplo.csv') as file:
    # Lemos todas as linhas do arquivo e criamos uma lista
    linhas = file.readlines()

# Criamos um reader CSV a partir das linhas do arquivo, com os campos nome e idade e delimitado por ;
reader = csv.DictReader(linhas, ['nome', 'idade'], delimiter=';')
for linha in reader:
    print(linha)

# Criamos um arquivo exemplo.csv com modo de escrita
with open('exemplo2.csv', 'w') as file:
    # Criamos um writer CSV para escrever no arquivo, com os campos carro e km
    writer = csv.DictWriter(file, ['carro', 'km'])
    # Escrevemos o header
    writer.writeheader()
    # Escrevemos as linhas
    writer.writerow(dict(carro="Ford", km=100))
    writer.writerow(dict(carro='VW', km=200))

