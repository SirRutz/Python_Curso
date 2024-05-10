# Crie um programa para entrar com o raio de um círculo e imprimir sua respectiva área e comprimento de sua circunferência. Declare uma constante para assumir o valor aproximado de PI.

raio = float(input('Digite o raio do círculo: '))
pi = 3.14

print('A área desse círculo é de:', pi *(raio*raio))
print('O comprimento desse círculo é de:',(2*pi)*raio)