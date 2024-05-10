# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def funcao(argumento):
    if argumento > 0:
     return 'P'
    elif argumento <=0:
     return 'N'
        
input = int(input('Digite um número para descobrir se ele é P ou N: '))
print(f'O numero {input} é {funcao(input)}')

