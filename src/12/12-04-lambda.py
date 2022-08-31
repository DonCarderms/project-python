maiuscula = lambda x:x.upper()
minuscula = lambda x:x.lower()
capital = lambda x:x.capitalize()

lista = ['Texto 01','Aluno 02','Carro 03','Animal 04',
'Flor 05','Cor 06', 'Avião 07']

funcoes = [maiuscula, minuscula, capital]

for item in lista:
    funcao = funcoes.pop(0)
    valor=funcao(item)
    print(item, funcao, valor)
    funcoes.append(funcao)
