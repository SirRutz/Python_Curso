# Escreva um programa que pergunte o ano de nascimento de uma pessoa e diga se ele é maior de idade

ano_atual = 2023
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - nascimento

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')





