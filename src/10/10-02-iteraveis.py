st = "STRING COM TAMANHO VARIÁVEL"
se = set([1,2,3,True,'A'])
li = list([1,2,3,True,'A'])
di = dict(nome='Guionardo',idade=45)

for item in li:
    print(item)
    li.append(1)
else:
    print('* FIM *')