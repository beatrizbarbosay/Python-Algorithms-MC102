#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
#####################################################
# Leitura da matriz
n = int(input())
matriz = [input().split() for _ in range(n)]
time1 = input()
if time1 == 'azul':
    time2= 'vermelho'
else:
    time1= 'vermelho'
    time2= 'azul'
jogadores = int(input())
matriz2 = [input().split() for _ in range(jogadores)]
item = pontototal1= pontototal2 = 0
for item in range(len(matriz2)):
    if item%2 == 0: #processamento de jogo para o primeiro time
        comando0 = matriz2[item]
        setas = list(str(comando0[0])) #lista em que cada direção é um item
        i = j = ponto1 = 0
        for direcao in range(len(setas)):
            if setas[direcao]=='L':
                j+=1
            elif setas[direcao] == 'O':
                j-=1
            elif setas[direcao] == 'N':
                i-=1
            elif setas[direcao] == 'S':
                i+=1
            loc = matriz[i][j]
            if loc == '*':
                ponto1 += 1
                matriz[i][j]='.'
        pontototal1+=ponto1
    elif item%2 != 0: #processamento de jogo para o segundo time
        comando0 = matriz2[item]
        setas = list(str(comando0[0])) #lista em que cada direção é um item
        i = j = ponto2 = 0
        for direcao in range(len(setas)):
            if setas[direcao]=='L':
                j+=1
            elif setas[direcao] == 'O':
                j-=1
            elif setas[direcao] == 'N':
                i-=1
            elif setas[direcao] == 'S':
                i+=1
            loc = matriz[i][j]
            if loc == '*':
                ponto2 += 1
                matriz[i][j]= '.'
        pontototal2+=ponto2
if time1== 'azul':
    print(f'Tesouros encontrados pelo time {time1}: {pontototal1}')
    print(f'Tesouros encontrados pelo time {time2}: {pontototal2}')
else:
    print(f'Tesouros encontrados pelo time {time2}: {pontototal2}')
    print(f'Tesouros encontrados pelo time {time1}: {pontototal1}')
if pontototal1>pontototal2:
    print(f'Vitoria do time {time1}')
elif pontototal1==pontototal2:
    print('Empate')
else:
    print(f'Vitoria do time {time2}')