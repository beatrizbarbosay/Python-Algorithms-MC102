#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome:
# RA:
#####################################################

"""
Esta função recebe como parâmetro uma matriz que representa o tabuleiro,
uma posição atual (linha_atual, coluna_atual) no tabuleiro, uma posição
final (linha_fim, coluna_fim) desejada e o parâmetro cor indica a cor da
última posição visitada no caminho.
O retorno esperado para a função é um valor booleano, com True indicando
que foi possível encontrar um caminho e False indicando que não existe um
caminho.
"""

def caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim):
  i = linha_atual
  j= coluna_atual
  loc = tabuleiro[i][j]
  encontrou = True
  while loc != tabuleiro[linha_fim][coluna_fim]:
    if loc == 0:
      if loc[i+1][j]==1:
        loc = loc[i+1][j]
      elif loc[i-1][j]==1:
        loc = loc[i-1][j]
      elif loc[i][j+1]==1:
        loc= loc[i][j+1]
      elif loc[i][j-1]==1:
        loc = loc[i][j-1]
      if loc == tabuleiro[linha_fim][coluna_fim]:
        encontrou = True
      else:
        encontrou = False
    if loc == 1:
      if loc[i+1][j]==0:
        loc = loc[i+1][j]
      elif loc[i-1][j]==0:
        loc = loc[i-1][j]
      elif loc[i][j+1]==0:
        loc= loc[i][j+1]
      elif loc[i][j-1]==0:
        loc = loc[i][j-1]
      if loc == tabuleiro[linha_fim][coluna_fim]:
        encontrou = True
      else:
        encontrou = False
  return encontrou


L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

linha_atual = l1
coluna_atual = c1
linha_fim = l2
coluna_fim= c2

if caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim) == True:
  print("caminho encontrado")

if caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim)== False:
  print("caminho nao encontrado")