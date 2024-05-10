# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 8 dígitos, acrescentando o ‘9' na frente. O usuário pode informar o número com ou sem o traço separador.

telefone = input('Digite seu número de telefone: ')
telefoneSemSeparador = telefone.replace('-','')

if len(telefoneSemSeparador) == 8:
    print(f'9{telefoneSemSeparador}')

