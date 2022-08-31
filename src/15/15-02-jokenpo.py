from jokenpo_utils import (avaliar_jogada, gerar_jogada_pc, imprimir_placar,
                           instrucoes, perguntar_jogada_humano, simnao)


def main():
    '''Função principal do programa'''
    if not simnao('Deseja começar?'):
        return

    instrucoes()
    n_jogada = p_pc = p_humano = 0

    while n_jogada < 7:
        print('\nJogada #', n_jogada+1)
        n_jogada += 1
        j_pc = gerar_jogada_pc()
        j_hu = perguntar_jogada_humano()
        if not j_hu:
            break
        resultado = avaliar_jogada(j_pc, j_hu)
        if resultado == -1:
            p_pc += 1
        elif resultado == 1:
            p_humano += 1

    imprimir_placar(p_pc, p_humano)


if __name__ == '__main__':
    main()
