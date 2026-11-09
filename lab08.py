###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
###################################################
palavra = input()
lpalavra = list(palavra)
acertou = False
for k in range(6):
    item=0
    tentativa = input()
    lfinal = ['x']*(len(lpalavra))
    if tentativa == palavra:
        print(palavra.upper())
        print("Resposta correta")
        acertou = True
        break
    else:
        while item<len(lpalavra):
            ltentativa= list(tentativa)
            if ltentativa[item] not in lpalavra:
                lfinal[item]=str('_')
            elif ltentativa[item] in lpalavra and ltentativa[item]!=lpalavra[item]:
                lfinal[item]=ltentativa[item]
            elif ltentativa[item]==lpalavra[item]:
                lfinal[item]=ltentativa[item].upper()
            item+=1
    print(''.join(lfinal))
if acertou == False:
    print("Palavra correta:", palavra)

