# Faça um programa em Python (utilize a estrutura for) que leia 10 valores inteiros e:• Encontre e mostre o maior valor • Encontre e mostre o menor valor • Calcule e mostre a média dos números lidos
 
valores = []

for numero in range(10):
    numero = int(input("Digite um numero inteiro: "))
    valores.append(numero)

media = (sum(valores)) / 10

valores.sort()
print(f'O maior valor é: {valores[-1]}')
print(f'O menor valor é: {valores[0]}')
print(f'A média desses valores é: {media}')
