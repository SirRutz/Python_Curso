# Crie um programa para entrar com a base a altura de um retângulo e imprimir respectivamente o perímetro e a área correspondente. Essas fórmulas podem ser encontradas na Wikipédia.

base = float(input('Digite a base do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

print('O perímetro desse retângulo é:', (base*2) + (altura*2))
print('A área desse retângulo é:', base * altura)