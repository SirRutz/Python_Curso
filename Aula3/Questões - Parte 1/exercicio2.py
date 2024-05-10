# Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2: 
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1
    
print('O maior número é:', maior)
print('O menor número é:', menor)
