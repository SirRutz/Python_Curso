# Crie um programa para ler dois valores para as variáveis A e B, respectivamente. Efetuar a troca dos valores de forma que a variável A passe a ter o valor da variável B e que a variável  B passe a ter o valor da variável A. Considere A e B como variáveis do tipo inteiro. Apresente os valores trocados.

variavelA = int(input('Digite um número inteiro: '))
variavelB = int(input('Digite outro número inteiro: '))

variavelA, variavelB = variavelB, variavelA

print('Após a troca de valores, A:',variavelA, 'e B:',variavelB)



