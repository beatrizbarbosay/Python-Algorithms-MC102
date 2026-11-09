##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Ana Beatriz Barbosa Yoshida
# RA:245609
##################################################
# Leitura do valor da hora
V = int(input())
# Leitura do numero de dias trabalhados na semana
D = int(input())
# Leitora e processamento dos periodos de trabalho de cada dia
horas_dia = horas_t = extra = 0
for i in range (D):
    horas_dia = 0
    quantidade=int(input())

    for j in range (quantidade): #calculo das horas diarias
        comeco= int(input())
        fim= int(input())
        horas_dia += fim - comeco

    if horas_dia>8: #horas extras diarias
        extra+= horas_dia - 8
    else:
        extra+=0

    horas_t += horas_dia  # horas totais trabalhadas
if horas_t-extra>44: #horas extras totais
    extra2= horas_t - 44
    salario= horas_t*V + (extra2)*(V/2)
else:
    salario = horas_t * V + (extra) * (V / 2)
    extra2=extra

print("Horas trabalhadas:", horas_t)
print("Horas extras:", extra2)
print("Valor devido: R$ {:0.2f}".format(salario))
