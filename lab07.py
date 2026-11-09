###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
###################################################
# Leitura das tropas de defesa
n_defesa= int(input())
defesa=[]
while len(defesa)<n_defesa:
    defesa.append(int(input()))
# Leitura das tropas de ataque
n_ataque= int(input())
ataque=[]
while len(ataque)<n_ataque:
    ataque.append(int(input()))
# Processamento da guerra
vitoria=0
for rodada in range(len(defesa)-len(ataque)):
    ganho = perda = empate = 0
    for n in range(len(ataque)):
        if defesa[n+rodada]<ataque[n]:
            ganho+=1
        elif defesa[n+rodada]>ataque[n]:
            perda+=1
        else:
            empate+=1
    if ganho>perda:
        rodada+=1
        print('Vitória posicionando as tropas a partir da posição',rodada)
        vitoria=1
        break
if vitoria==0:
    print('Derrota')