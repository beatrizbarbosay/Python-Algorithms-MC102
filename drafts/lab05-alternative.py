##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome:
# RA:
##################################################

# Leitura do valor da hora
V = int(input())
# Leitura do numero de dias trabalhados na semana
D = int(input())
# Leitora e processamento dos periodos de trabalho de cada dia
horas_trabalhadas = 0
e=0 #horas extras semanais
salario = 0
for i in range (D):
    p = int(input()) #período trabalhado
    horas_dias = 0
    for j in range (p):
        c = int(input()) #começo do período
        f = int(input()) #fim do período
        horas_dias += (f - c)
    if horas_dias>8:
        e += (horas_dias - 8)
    horas_trabalhadas += horas_dias
e2=0
if (horas_trabalhadas-e) > 44:
    e2 = horas_trabalhadas - 44
    salario= (e2)*(V/2) + horas_trabalhadas*V
else:
    salario= (e)*(V/2) + horas_trabalhadas*V
    e2 = e

print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", e2)
print("Valor devido: R$ {:0.2f}".format(salario))