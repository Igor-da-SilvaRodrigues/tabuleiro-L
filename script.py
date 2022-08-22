# q1
# python 3.10
# Igor da Silva Rodrigues
#   ---------
#   | 0 | 1 |
#   | 2 | 3 |
#   ---------

import numpy as np
import math


class Tabuleiro:
    def __init__(self, n):
        # uma matriz com 2^2n quadrados tem lado igual a sqrt(2^2n)
        lado = int(np.sqrt(2 ** (2 * n)))
        self.tabuleiro = np.zeros((lado, lado))
        self.dimensao = n

    def set_tabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro
        lado = len(tabuleiro)
        self.dimensao = int(math.log(lado, 2))

    def __repr__(self):
        return str(self.tabuleiro)


def set_campo(coords, tabuleiro, line_range, column_range, value=1):
    """
    :param coords: as coordenadas da casa a ser alterada, no formato (1,2,3)
    :param tabuleiro: uma matriz nxn representando um tabuleiro, use a classe Tabuleiro para gerar, e passe T.tabuleiro
    :param line_range: deve ser range(len(tabuleiro))
    :param column_range: deve ser range(len(tabuleiro[0])), deve ser igual a line_range
    :param value: valor a ser atribuido a casa
    :return:
    """
    if len(coords) == 0:
        tabuleiro[line_range.start][column_range.start] = value
        return

    half_line = line_range.start + int((line_range.stop - line_range.start) / 2)
    half_column = column_range.start + int((column_range.stop - column_range.start) / 2)

    target = coords[0]
    newcoords = coords[1:]

    # q0 = range(half_tam)           range(half_tam)
    # q1 = range(half_tam)           range(half_tam, tam)
    # q2 = range(half_tam, tam)      range(half_tam)
    # q3 = range(half_tam, tam)      range(half_tam, tam)
    new_line_range = None
    new_column_range = None

    match target:
        case 0:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(column_range.start, half_column)
        case 1:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(half_column, column_range.stop)
        case 2:
            new_line_range = range(half_line, line_range.stop)
            new_column_range = range(column_range.start, half_column)
        case 3:
            new_line_range = range(half_line, line_range.stop)
            new_column_range = range(half_column, column_range.stop)
        case _:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(column_range.start, half_column)

    set_campo(newcoords, tabuleiro, new_line_range, new_column_range)


def get_campo(coords, tabuleiro, line_range, column_range):
    """
    :param coords: as coordenadas da casa a ser retornada, no formato (1,2,3)
    :param tabuleiro: uma matriz nxn representando um tabuleiro, use a classe Tabuleiro para gerar, e passe T.tabuleiro
    :param line_range: deve ser range(len(tabuleiro))
    :param column_range: deve ser range(len(tabuleiro[0])), deve ser igual a line_range
    :return: O valor da casa referenciada :int
    """
    if len(coords) == 0:
        return tabuleiro[line_range.start][column_range.start]

    half_line = line_range.start + int((line_range.stop - line_range.start) / 2)
    half_column = column_range.start + int((column_range.stop - column_range.start) / 2)

    target = coords[0]
    newcoords = coords[1:]

    # q0 = range(half_tam)           range(half_tam)
    # q1 = range(half_tam)           range(half_tam, tam)
    # q2 = range(half_tam, tam)      range(half_tam)
    # q3 = range(half_tam, tam)      range(half_tam, tam)
    new_line_range = None
    new_column_range = None

    match target:
        case 0:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(column_range.start, half_column)
        case 1:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(half_column, column_range.stop)
        case 2:
            new_line_range = range(half_line, line_range.stop)
            new_column_range = range(column_range.start, half_column)
        case 3:
            new_line_range = range(half_line, line_range.stop)
            new_column_range = range(half_column, column_range.stop)
        case _:
            new_line_range = range(line_range.start, half_line)
            new_column_range = range(column_range.start, half_column)

    return get_campo(newcoords, tabuleiro, new_line_range, new_column_range)


# Q1 A))================================================================================================================
def completa_exceto(tabuleiro, exceto, list_l):
    """
    Verifica se as peças fornecidas preenchem completamente o tabuleiro exceto por uma casa especificada

    :param tabuleiro: o tabuleiro a ser checado
    :param exceto: Uma tuple representando a casa que não deve ser preenchida
    :param list_l: Uma lista contendo peças em L no formato [[(1,3),(1,1),(1,2)], [(1,3),(1,1),(1,2)]]
    :return: True se as peças fornecidas preencham completamente o tabuleiro <strong>exceto</strong> a casa 'exceto'
    """
    copia_tabuleiro = Tabuleiro(tabuleiro.dimensao).tabuleiro

    line_range = range(len(copia_tabuleiro))
    column_range = range(len(copia_tabuleiro[0]))
    for peca in list_l:
        for coord in peca:
            set_campo(coord, copia_tabuleiro, line_range, column_range)

    preto = get_campo(exceto, copia_tabuleiro, line_range, column_range)

    if preto == 1:
        return False  # a casa 'exceto' foi preenchida por alguma das peças

    set_campo(exceto, copia_tabuleiro, line_range, column_range, 2)
    for linha in copia_tabuleiro:
        for casa in linha:
            if casa == 0:
                return False  # alguma casa não foi preenchida

    return True


# Q1 B)=================================================================================================================
def preencher_tabuleiro_exceto(dimensao, exceto):
    """
    Retorna uma lista de peças em L, que preenchem um tabuleiro de dimensão n exceto por uma casa especificada.

    :param dimensao: a dimensao do tebuleiro
    :param exceto:  o endereço da casa a não ser preenchida, len(exceto) deve ser igual a dimensao
    :return: uma lista de peças
    """
    if len(exceto) != dimensao:
        raise Exception("O endereço 'exceto' fornecido não é compatível ou inexisente em um tabulerio de dimensão "
                        "'dimensao'. Cheque se o tamanho do endereço fornecido está correto.")

    if dimensao <= 1:
        peca = [(0,), (1,), (2,), (3,)]
        peca.remove(exceto)
        return [peca]  # retorna a peça em L que preenche o menor possivel quadrante sem cobrir a peça marcada
    # os valores dessa tuple devem ser concatenados com o valor do quadrante pai se este existir.

    # 0333...  1222...
    # 2111...  3000...
    # os quadrados centrais seguem um padrão de endereçamento, ilustrado acima.

    flag = exceto[0]  # flag que identifica qual quadrante exterior deve preencher o quadrado central
    # todos os quadrados centrais que não possuem essa flag serão marcados como 'exceto' antes da recursão
    # a flag é a primeira coordenada da casa exceto.
    casas_centro = [[0], [1], [2], [3]]
    casas_centro.remove([flag])

    for casa in casas_centro:
        for i in range(dimensao - 1):
            match casa[0]:
                case 0:
                    casa.append(3)
                case 1:
                    casa.append(2)
                case 2:
                    casa.append(1)
                case 3:
                    casa.append(0)

    peca_centro_ = []
    for casa in casas_centro:
        peca_centro_.append(tuple(casa))

    # nesse ponto da execução, peca_centro_ representa o endereço de todas as casas do centro que não possuem flag
    # essas casas devem ser agrupadas em uma unica peça L

    # ao passar a recursão, todos os endereços devem ter o digito mais significativo removido, ex: 211 se tornará 11
    # ao passar a recursão, a dimensão deverá ser reduzida em 1

    pecas = [peca_centro_]  # array de peças

    q0 = preencher_tabuleiro_exceto(dimensao - 1, peca_centro_[0][1:])  # q0
    pq0 = peca_centro_[0][:1]
    q1 = preencher_tabuleiro_exceto(dimensao - 1, peca_centro_[1][1:])  # q1
    pq1 = peca_centro_[1][:1]
    q2 = preencher_tabuleiro_exceto(dimensao - 1, peca_centro_[2][1:])  # q2
    pq2 = peca_centro_[2][:1]
    q3 = preencher_tabuleiro_exceto(dimensao - 1, exceto[1:])  # q3
    pq3 = exceto[:1]

    new_q = []  # lista de peças
    new_peca = []  # lista de casas
    for peca in q0:
        for casa in peca:
            new_peca.append(pq0 + casa)
        new_q.append(new_peca)
        new_peca = []
    q0 = new_q

    new_q = []
    new_peca = []
    for peca in q1:
        for casa in peca:
            new_peca.append(pq1 + casa)
        new_q.append(new_peca)
        new_peca = []
    q1 = new_q

    new_q = []
    new_peca = []
    for peca in q2:
        for casa in peca:
            new_peca.append(pq2 + casa)
        new_q.append(new_peca)
        new_peca = []
    q2 = new_q

    new_q = []
    new_peca = []
    for peca in q3:
        for casa in peca:
            new_peca.append(pq3 + casa)
        new_q.append(new_peca)
        new_peca = []
    q3 = new_q

    for peca in q0:
        pecas.append(peca)

    for peca in q1:
        pecas.append(peca)

    for peca in q2:
        pecas.append(peca)

    for peca in q3:
        pecas.append(peca)

    return pecas  # retorna a lista de pecas em L que completam o tabuleiro exceto 'exceto'


def main():
    t = Tabuleiro(3)
    tab = t.tabuleiro
    coordenadas = tuple([3])
    exceto = (3, 0, 1)

    print(tab)
    print('\n')

    pecas = preencher_tabuleiro_exceto(t.dimensao, exceto)
    print(pecas)
    print(completa_exceto(t, exceto, pecas))


if __name__ == '__main__':
    main()
