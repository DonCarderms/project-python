pessoas = [
    dict(nome='Zé', tipo=1),
    dict(nome='Ana', tipo=2),
    dict(nome='Carlos', tipo=3),
    dict(nome='Mário', tipo=1),
    dict(nome='Zefa', tipo=2),
    dict(nome='Ben', tipo=3),
    dict(nome='Xerxes', tipo=1),
    dict(nome='Bolsonaro', tipo=4)
]

acoes = {
    1: lambda x: 'TIPO 1 '+x['nome'],
    2: lambda x: 'Outro Tipo '+x['nome'],
    3: lambda x: 'Diferente '+x['nome'],
    0: print
}

for pessoa in pessoas:
    print(acoes.get(pessoa['tipo'], acoes[0])(pessoa))
