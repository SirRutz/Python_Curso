# Faça um algoritmo para ler um número inteiro e informar se este é menor, maior ou igual 10.

numero = int(input('Insira um número inteiro: '))

if numero <10:
    print(numero, 'é menor que 10')
elif numero == 10:
    print(numero,'é igual a 10')
elif numero >10:
    print(numero, 'é maior que 10')