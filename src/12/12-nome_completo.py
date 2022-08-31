def nome_completo(prenome: str, nome_do_meio: str = '', sobrenome: str = ''):
    nome = prenome.strip()
    if nome_do_meio:
        nome += ' '+nome_do_meio.strip()
    if sobrenome:
        nome += ' '+sobrenome.strip()
    return nome


def criar_usuario(nome, senha, **opcoes):
    usuario = {'nome': nome, 'senha': senha}
    usuario.update(opcoes)
    return usuario


print(nome_completo('José', 'Silva'))


def separar_nome(nome):
    nome = nome.split()
    if len(nome) > 1:
        return nome[0], nome[-1]
    return nome[0], ''


nome, sobrenome = separar_nome('José Ferreira da Silva')
print(nome, sobrenome)

usuario = criar_usuario('zé', '1234', admin=True,
                        ativo=True, data_admissao='2022-08-12')
print(usuario)