# Dadas duas tuplas L1 e L2, com n e m valores inteiros, respectivamente, escreva um programa que concatene as tuplas L1 e L2 em uma nova tupla L3. Em seguida, imprima a tupla L3 ordenada de maneira crescente e decrescente.

valorUm = (2, 5, 9, 10, 11, 4, 2)
valorDois = (4, 6, 1, 2, 10, 15, 1)

valorTres = list(valorUm + valorDois)

valorTres.sort()
print(f'A tupla em ordem crescente é: {tuple(valorTres)}')

valorTres.reverse()
print(f'A tupla em ordem decrescente é: {tuple(valorTres)}')



