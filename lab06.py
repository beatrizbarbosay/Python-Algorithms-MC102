##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Ana Beatriz Barbosa Yoshida RA: 245609
##################################################
# Leitura da torre de panquecas

torre = [int(panqueca) for panqueca in input().split()]
espatula=1
while espatula !=0:
    espatula = int(input())
    torren=torre[:espatula]
    torren.reverse()
    torre=torren+torre[espatula:]
if torre == sorted(torre):
    print ('Torre estavel')
else:
    print('Torre instavel')


