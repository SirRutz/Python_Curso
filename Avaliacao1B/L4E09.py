contadorBranco = 0
contadorNulo = 0
contadorKiko = 0
contadorChaves = 0
contadorChiquinha = 0


votos = int(input('Digite seu voto (1-Branco, 2-Nulo, 3-Kiko, 4-Chaves, 5-Chiquinha): '))
if votos == 1:
    contadorBranco += 1
if votos == 2:
    contadorNulo += 1
if votos == 3:
    contadorKiko += 1
if votos == 4:
    contadorChaves += 1
if votos == 5:
    contadorChiquinha += 1

while votos != 666:
 votos = int(input('Digite seu voto (1-Branco, 2-Nulo, 3-Kiko, 4-Chaves, 5-Chiquinha): '))
 if votos == 1:
    contadorBranco += 1
 if votos == 2:
    contadorNulo += 1
 if votos == 3:
    contadorKiko += 1
 if votos == 4:
    contadorChaves += 1
 if votos == 5:
    contadorChiquinha += 1
 
 if votos <=0 or votos >5:
     break
 elif votos == 666:
     break

print(f'Branco: {contadorBranco} Nulo: {contadorNulo} Kiko: {contadorKiko} Chaves: {contadorChaves} Chiquinha: {contadorChiquinha}')