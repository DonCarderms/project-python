def criar_usuario(nome, senha, **opcoes):
    """
    O argumento opcoes vai receber os parametros nomeados tipados como um dict
    Nesse exemplo, o dict opcoes vai atualizar o dict usuario    
    """
    usuario = {'nome': nome, 'senha': senha}
    usuario.update(opcoes)
    return usuario


usuario = criar_usuario('zé', '1234', admin=True,
                        ativo=True,
                        data_admissao='2022-08-12')
print(usuario)
