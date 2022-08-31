from random import choice

opcoes = dict(
    p='pedra',
    a='papel',
    t='tesoura')


def instrucoes():
    print("""*** JOKENPO ***
Neste jogo, vamos combater escolhendo três objetos. 
Pedra, Papel e Tesoura.

Pedra ganha de Tesoura
Tesoura ganha de Papel
Papel ganha de Pedra

Vamos começar!
    """)


def gerar_jogada_pc():
    jogada_pc = choice(list(opcoes.keys()))
    print('Já escolhi minha jogada')
    return jogada_pc


def pedir_jogada_humano():
    print('***\nEscolha sua jogada\n')
    print(
        '\n'.join([
            f'{codigo}: {opcao}'
            for codigo, opcao
            in opcoes.items()]))
    while True:
        opcao = input('?').strip().lower()
        if opcao not in opcoes:
            if input('Deseja continuar jogando (S/N)?').strip() != 'S':
                return None, False
            print('Informe uma das opções: ', opcoes)
            continue
        return opcao, True


def verificar_ganhador(jogada_pc, jogada_humano):
    estado = ''
    print(
        f'Eu escolhi "{opcoes[jogada_pc]}" e você escolheu "{opcoes[jogada_humano]}"')

    if jogada_pc == jogada_humano:
        # Empate
        estado = 'E'
        mensagem = f'{opcoes[jogada_pc]} == {opcoes[jogada_humano]}'

    # Pedra ganha de tesoura
    # Tesoura ganha de papel
    # Papel ganha de pedra
    elif (jogada_pc == 'p' and jogada_humano == 't') or \
        (jogada_pc == 't' and jogada_humano == 'a') or \
            (jogada_pc == 'a' and jogada_humano == 'p'):
        estado = 'P'
        mensagem = f'{opcoes[jogada_pc]} ganha de {opcoes[jogada_humano]}'
    else:
        estado = 'H'
        mensagem = f'{opcoes[jogada_pc]} perde de {opcoes[jogada_humano]}'

    print(mensagem.capitalize(),
          dict(
              P='Eu ganhei',
              H='Você ganhou',
              E='Nós empatamos'
    ).get(estado))

    return estado


def placar(pc, humano):
    print(' PLACAR '.center(20, '*'))
    print(f' PC     {pc:3d}')
    print(f' HUMANO {humano:3d}')
    if pc == humano:
        print(' EMPATOU '.center(20, '#'))
    elif pc > humano:
        print(' EU GANHEI '.center(20, '#'))
    else:
        print(' VOCÊ GANHOU! '.center(20, '#'))


jogando = True
pontos_pc = pontos_humano = 0
instrucoes()

while jogando:
    print('-'*20)
    pc = gerar_jogada_pc()
    humano, jogando = pedir_jogada_humano()
    if not jogando:
        break
    quem_ganhou = verificar_ganhador(pc, humano)
    if quem_ganhou == 'P':
        pontos_pc += 1
    elif quem_ganhou == 'H':
        pontos_humano += 1

placar(pontos_pc, pontos_humano)
