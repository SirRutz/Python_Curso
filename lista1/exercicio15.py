# Crie um programa e declare uma constante PI (use 4 casas após a vírgula). Dados o raio e a altura, calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: volume = PI * r2* altura

pi = 3.1415
raio = float(input('Digite o raio: '))
altura = float(input('Digite a altura: '))
volume = pi * (raio*raio) * altura

print ('O volume é igual a: {:.1f}'.format(volume))

