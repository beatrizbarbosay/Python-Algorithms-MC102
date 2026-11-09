###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Ana Beatriz Barbosa Yoshida
# RA: 245609
###################################################
d=int(input('')) #dia da semana
h=int(input('')) #hora
m=int(input('')) #minuto
e=input('') #estudante?
p= input('') #pagamento
# domingo
if d==1 and (e=='S'):
    print('Valor do ingresso: R$ 15,00')
elif d==1 and (e=='N') and (p=='C'):
    print('Valor do ingresso: R$ 21,00')
elif d==1 and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 30,00')
# segunda e terça
elif (d==2 or d==3 or d==4) and (h<18 or (h==18 and m<=30)) and (e=='S' or p=='C'):
    print('Valor do ingresso: R$ 7,50')
elif (d==2 or d==3 or d==4) and (h<18 or (h==18 and m<=30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 15,00')
elif (d==2 or d==3) and (h>18 or (h==18 and m>30)) and (e=='S' or p=='C'):
    print('Valor do ingresso: R$ 10,00')
elif (d==2 or d==3) and (h>18 or (h==18 and m>30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 20,00')
#quarta
elif (d==4 or d==5) and (h>18 or (h==18 and m>30)) and (e=='S' or p=='C'):
    print('Valor do ingresso: R$ 15,00')
elif (d==4 or d==5) and (h>18 or (h==18 and m>30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 30,00')
#quinta
elif (d==5 or d==6) and (h<18 or (h==18 and m<=30)) and (e=='S' or p=='C'):
    print('Valor do ingresso: R$ 10,00')
elif (d==5 or d==6) and (h<18 or (h==18 and m<=30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 20,00')
#sexta
elif (d==6 or d==7) and (h>18 or (h==18 and m>30)) and (e=='S'):
    print('Valor do ingresso: R$ 20,00')
elif d==6 and (h>18 or (h==18 and m>30)) and (e=='N') and (p=='C'):
    print('Valor do ingresso: R$ 28,00')
elif (d==6 or d==7) and (h>18 or (h==18 and m>30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 40,00')
#sábado
elif d==7 and (h<18 or (h==18 and m<=30)) and (e=='S'):
    print('Valor do ingresso: R$ 15,00')
elif d==7 and (h<18 or (h==18 and m<=30)) and (e=='N') and (p=='C'):
    print('Valor do ingresso: R$ 24,00')
elif d==7 and (h<18 or (h==18 and m<=30)) and (e=='N') and (p=='D'):
    print('Valor do ingresso: R$ 30,00')
elif d==7 and (h>18 or (h==18 and m>30)) and (e=='N') and (p=='C'):
    print('Valor do ingresso: R$ 32,00')



