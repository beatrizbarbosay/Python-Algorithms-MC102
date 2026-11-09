#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
#####################################################

"""
Esta função recebe como parâmetro uma matriz que representa o tabuleiro,
uma posição atual (linha atual, coluna atual) no tabuleiro, uma posição
final (linha_fim, coluna_fim) desejada e o parâmetro cor indica a cor da
última posição visitada no caminho.
O retorno esperado para a função é um valor booleano, com True indicando
que foi possível encontrar um caminho e False indicando que não existe um
caminho.
"""


def caminho(tabuleiro, latual, catual, lfim, cfim):
    if latual == lfim and catual == cfim:
        return True
    prox_posicoes = [
        (latual + 1, catual),
        (latual - 1, catual),
        (latual, catual + 1),
        (latual, catual - 1)]
    cor_atual = tabuleiro[latual][catual]
    tabuleiro[latual][catual] = "x"
    for prox_linha, prox_coluna in prox_posicoes:
        if prox_linha == -1 or prox_linha == len(tabuleiro) or prox_coluna == -1 or prox_coluna == len(tabuleiro[0]):
            continue
        prox_cor = tabuleiro[prox_linha][prox_coluna]
        if prox_cor == cor_atual or prox_cor == "x":
            continue
        if caminho(tabuleiro, prox_linha, prox_coluna, lfim, cfim):
            return True
    return False


# Leitura dos dados
L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

# Verificação se existe um caminho
if caminho(tabuleiro, l1, c1, l2, c2):
    print("caminho encontrado")
else:
    print("caminho nao encontrado")