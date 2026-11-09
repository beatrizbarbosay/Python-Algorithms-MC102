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

def caminho(tabuleiro, latual, catual, testetab):
    i = latual
    j = catual
    loc = tabuleiro[i][j]
    if loc == 0:
        if loc[i+ 1][j] == 1 and testetab[i+1][j]==0:
            loc = loc[i+ 1][j]
            testetab[i + 1][j] = 2
            latual +=1
        elif loc[i - 1][j] == 1 and testetab[i - 1][j]==0:
            loc = loc[i - 1][j]
            testetab[i - 1][j] = 2
            latual -= 1
        elif loc[i][j + 1] == 1 and testetab[i][j+1]==0:
            loc = loc[i][j + 1]
            testetab[i][j+1] = 2
            catual+=1
        elif loc[i][j - 1] == 1 and testetab[i][j-1]==0:
            loc = loc[i][j - 1]
            testetab[i][j-1] = 2
            catual -=1
    elif loc == 1:
        if loc[i+ 1][j] == 0 and testetab[i+1][j]==0:
            loc = loc[i+ 1][j]
            testetab[i + 1][j] = 2
            latual +=1
        elif loc[i - 1][j] == 0 and testetab[i - 1][j]==0:
            loc = loc[i - 1][j]
            testetab[i - 1][j] = 2
            latual -= 1
        elif loc[i][j + 1] == 0 and testetab[i][j+1]==0:
            loc = loc[i][j + 1]
            testetab[i][j+1] = 2
            catual+=1
        elif loc[i][j - 1] == 0 and testetab[i][j-1]==0:
            loc = loc[i][j - 1]
            testetab[i][j-1] = 2
            catual -=1
    return latual,catual,testetab

L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

testetab = []
nex = len(tabuleiro)
mex = len(tabuleiro[0])
for i in range(nex):
    linhatest = [int(0) for l in range(mex)]
    testetab.append(linhatest)

(latual,catual,testetab)= caminho(tabuleiro, l1, c1, testetab)

encontrou = False
while tabuleiro[latual][catual] != tabuleiro[l2][c2]:
    caminho(tabuleiro, latual, catual, testetab)
    (latual,catual,testetab)=caminho(tabuleiro, latual, catual, testetab)
    if tabuleiro[latual][catual]==tabuleiro[l2][c2]:
        encontrou =True
        break

if encontrou== True:
    print("caminho encontrado")
if encontrou == False:
    print("caminho nao encontrado")