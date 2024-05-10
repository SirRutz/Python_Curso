
# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. Armazene os números em uma lista, depois percorra esta lista alimentando outras duas listas, uma com números pares e outra com números ímpares. Ordene e imprima os números em ordem crescente e some os valores e imprima o resultado.
 
par = []
impar = []
tudo = []

while True:
    num = int(input('Digite um numero inteiro (0 para sair): '))
    if num == 0:
        break
    tudo.append(num)
    print(tudo)

for num in tudo:
    if num %2 != 0:
      impar.append(num)

for num in tudo:
    if num %2 == 0:
      par.append(num)

impar.sort()
print('Dentres esses números, é impar:',impar)

par.sort()
print('Dentre esses números, é par:',par)

soma_par = sum(par)
soma_impar = sum(impar)

print(f'A soma dos numeros impares é:',soma_impar)
print(f'A soma dos numeros pares é:',soma_par)
