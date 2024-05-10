# Faça um programa em Python (utilize a estrutura while) que leia 10 valores inteiros e: • Encontre e mostre o maior valor • Encontre e mostre o menor valor • Calcule e mostre a média dos números lidos

numeros = []

while len(numeros) <10:
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)

numeros.sort
media = sum(numeros) / len(numeros)

print(f'O maior valor digitado foi: {numeros[-1]}')
print(f'O menor valor digitado foi: {numeros[0]}')
print(f'A media de valores calculados é {media}')