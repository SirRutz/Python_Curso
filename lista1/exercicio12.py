# Crie um programa para entrar com a razão de uma PA e o valor do primeiro termo. Calcular e imprimir o décimo termo da série.


pa = int(input('Defina o valor da PA: '))
termo = int(input('Defina o valor do primeiro termo: '))

decimoTermo = termo + (9 * pa)

print('décimo termo é:', decimoTermo)