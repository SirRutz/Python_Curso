# 5 - Crie um programa que dados o valor, a taxa e o tempo, efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula: prestação = valor + (valor*(taxa/100)*tempo)

valor = int(input('Digite o valor: '))
taxa = float(input('Digite a taxa: '))
tempo = int(input('Digite o tempo: '))
prestação = valor + (valor*(taxa/100)*tempo)
print(prestação)