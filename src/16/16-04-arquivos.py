from datetime import datetime
import json

# Abrimos o arquivo exemplo.json (em modo default somente leitura)
file = open('exemplo.json')
# Lemos o conteúdo do arquivo para a variável conteudo
conteudo = file.read()
# Fechamos o arquivo, liberando-o para o sistema operacional
file.close()

print(conteudo)

# Fazemos o parse do conteúdo do arquivo, convertendo para um dict
dados = json.loads(conteudo)
print(dados)

# Adicionamos um campo ao dict dados
dados['data_atualizacao'] = str(datetime.now())

# Abrimos o arquivo exemplo2.json em modo de escrita (se não existir, será criado. se existir será sobreescrito)
file = open('exemplo2.json', mode='w')
# Convertemos o dict dados em uma string
conteudo = json.dumps(dados, indent=2)
# Escrevemos o conteúdo no arquivo
file.write(conteudo)
# Fechamos o arquivo
file.close()
