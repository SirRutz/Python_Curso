# Escreva um programa em Python que receba uma string do usuário e mostre de trás para frente.

texto = str(input('Digite algo(0 para sair): '))

while texto != '0':  
    
    invertido = texto[::-1]
    print(f'O texto invertido é: {invertido}')
    texto = str(input('Digite algo(0 para sair): '))


