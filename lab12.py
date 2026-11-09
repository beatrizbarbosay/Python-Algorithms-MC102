###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
###################################################
def expansao(imagem_original,n,m):
    matrizexpansao = []
    nex = (2*n)-1
    mex = (2*m)-1
    for i in range(nex):
        linhaex = [int(l) for l in range(mex)]
        matrizexpansao.append(linhaex)
    for a in range(len(imagem_original)):
        for b in range(len(imagem_original[0])):
            matrizexpansao[2*a][2*b]=imagem_original[a][b]
    for c in range(len(matrizexpansao)):
        for d in range(len(matrizexpansao[0])):
            if c%2==0 and d%2!=0:
                matrizexpansao[c][d]= int(((matrizexpansao[c][d-1])+(matrizexpansao[c][d+1]))/2)
            elif c%2!=0 and d%2==0:
                matrizexpansao[c][d]= int(((matrizexpansao[c-1][d])+(matrizexpansao[c+1][d]))/2)
            elif c%2!=0 and d%2!=0:
                matrizexpansao[c][d]= int((((matrizexpansao[c-1][d-1]+matrizexpansao[c-1][d+1])/2)+((matrizexpansao[c+1][d-1]+matrizexpansao[c+1][d+1])/2))/2)
    imagem= matrizexpansao
    return imagem
def retracao(im,n,m):
    matrizr = []
    if len(im)%2==0:
        nre = int(n/2)
    elif len(im)%2!=0:
        nre = int((n+1)/2)
    if len(im[0])%2==0:
        mre = int(m/2)
    elif len(im[0])%2!=0:
        mre= int((m+1)/2)
    for i in range(nre):
        linhare = [int(l) for l in range(mre)]
        matrizr.append(linhare)
    matrizlista= []
    for a in range(0,len(im),2):
        addlista = []
        for b in range(0,len(im[0]),2):
            if a==(len(im)-1) and b==(len(im[0])-1):
                addlista.append(int(im[a][b]))
            elif b == len(im[0])-1:
                addlista.append(int((im[a][b] + im[a+1][b])/2))
            elif a==(len(im))-1:
                addlista.append(int((im[a][b]+ im[a][b+1])/2))
            else:
                addlista.append(int(((im[a][b]+ im[a][b+1] + im[a+1][b] + im[a+1][b+1])/4)))
        matrizlista.append(addlista)
    if len(matrizlista)==len(matrizr):
        imagem = matrizlista
    return imagem
def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))
# leitura da imagem
P2 = input()  # P2 - linha a ser ignorada
m, n = [int(x) for x in input().split()]
p255 = input()  # 255 - linha a ser ignorada
imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)
# leitura do tipo de redimensionamento
fazer = input()
if fazer == 'retracao':
    imagem = retracao(imagem_original,n,m)
elif fazer == 'expansao':
    imagem = expansao(imagem_original,n,m)
#impressão da imagem final
imprimir_imagem(imagem)