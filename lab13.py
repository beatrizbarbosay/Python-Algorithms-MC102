candidatos = {}

while True:
    candidato= input()
    if candidato == '0':
        break
    if candidato not in (candidatos.keys()):
        candidatos[candidato]=0
    if candidato in (candidatos.keys()):
        candidatos[candidato]+=1


sortedcandidatos1 = sorted(candidatos.items(), key=lambda x:x[1], reverse=True)
sortedcandidatos2 = dict(sortedcandidatos1)


for (candidatox,votos) in sortedcandidatos2.items():
    if candidatox != 'Branco' and candidatox != 'Nulo':
        print(candidatox,votos)

for (candidatox,votos) in sortedcandidatos2.items():
    if candidatox == 'Branco':
        print('Brancos',votos)

for (candidatox,votos) in sortedcandidatos2.items():
    if candidatox == 'Nulo':
        print('Nulos',votos)
