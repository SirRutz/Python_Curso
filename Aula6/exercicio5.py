# Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

numero = 6

while numero <=100:
    if numero % 2 == 0:
        print(numero)
    numero += 1