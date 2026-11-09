#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
#####################################################
'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''
# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())
# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())
def percorrer(k,y,pecax):
  naocabe=0
  for a in range(len(pecax)):
    for b in range(len(pecax[0])):
      if (tabuleiro[k + a][y + b] == 'X' and pecax[a][b] == 'X'):
        naocabe += 1
  return naocabe
def encaixe(pecax):
  pontonormal = 0
  for k in range(len(tabuleiro) - len(pecax) + 1):
    for y in range(len(tabuleiro[0])-len(pecax[0])+1):
      testar = percorrer(k,y,pecax)
      if testar==0:
        pontonormal += 1
  return pontonormal
def rodar90(pecax):
  peca90 = [[0 for m in range(len(pecax))] for n in range(len(pecax[0]))]
  for linha in range(len(pecax)):
    for coluna in range(len(pecax[0])):
      peca90[coluna][len(pecax) - 1 - linha] = pecax[linha][coluna]
  return peca90
peca1=encaixe(peca)
peca = rodar90(peca)
peca2=encaixe(peca)
peca = rodar90(peca)
peca3=encaixe(peca)
peca = rodar90(peca)
peca4=encaixe(peca)
print(peca1,peca2,peca3,peca4, sep = ',')


