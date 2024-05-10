# Construa um programa em Python utilizando os comandos aprendidos até agora para encontrar todos os números pares entre 1 e 100.

pares = []

for numero in range(101):
    if numero % 2 == 0:
     pares.append(numero)
    
print(pares)
