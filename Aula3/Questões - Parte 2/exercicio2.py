# Faça um algoritmo que receba um valor de uma compra e receba o numero de prestações, apresente o valor das prestações sem juros.

valor = int(input('Insira o valor do produto: '))
prestacao = int(input('Insira a quantidade de prestações: '))

print('O valor de sua compra em', prestacao,'prestações é:', valor/prestacao)
