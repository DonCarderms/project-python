from random import choice


OPCOES = {
    'p': 'Pedra',
    'a': 'pApel',
    't': 'Tesoura'
}


def simnao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in 'sn':
            return resposta == 's'
        print('ERRO: Informe S ou N!')


def instrucoes():
    print(' JOKENPO '.center(40, '*'),
          'Regras:',
          '* Pedra ganha de Tesoura',
          '* Tesoura ganha de pApel',
          '* pApel ganha de Pedra',
          '*'*40,
          sep='\n')


def gerar_jogada_pc():
    jogada_pc = choice(list(OPCOES.keys()))
    print('Minha vez. Já escolhi minha opção...')
    return jogada_pc


def perguntar_jogada_humano():
    while True:
        jogada_hu = input(
            f'Informe a sua jogada {list(OPCOES.keys())}:').strip().lower()
        if jogada_hu in OPCOES:
            return jogada_hu
        print(f'ERRO: opções',
              [f'{k} = {v}' for k, v in OPCOES.items()],
              sep='\n')
        if simnao('Deseja sair?'):
            return None


def avaliar_jogada(j_pc, j_hu):
    """Avalia a jogada retornando
    0 = Empate
    -1 = PC ganhou
    1 = Humano ganhou
    """
    if j_pc == j_hu:
        print('Empatamos com ', OPCOES[j_pc])
        return 0
    if ((j_pc == 'p' and j_hu == 't') or
        (j_pc == 't' and j_hu == 'a') or
            (j_pc == 'a' and j_hu == 'p')):
        mensagem = f'Eu ganhei. {OPCOES[j_pc]} ganha de {OPCOES[j_hu]}'
        r = -1
    else:
        mensagem = f'Você ganhou. {OPCOES[j_hu]} ganha de {OPCOES[j_pc]}'
        r = 1
    print(mensagem)
    return r


def imprimir_placar(p_pc, p_humano):
    if p_pc == p_humano:
        print(f'EMPATAMOS {p_pc} a {p_humano}')
    elif p_pc > p_humano:
        print(f'EU GANHEI DE {p_pc} a {p_humano}')
    else:
        print(f'VOCÊ GANHOU DE {p_humano} a {p_pc}')


if __name__ == '__main__':
    resposta = simnao('Deseja jogar jokenpo?')
