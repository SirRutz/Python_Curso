# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

stringUm = input('Digite algo: ')
stringDois = input('Digite algoI: ')

print(f'A string {stringUm} tem {len(stringUm)} caracteres de comprimento')
print(f'A string {stringDois} tem {len(stringDois)} caracteres de comprimento')

if len(stringUm) == len(stringDois):
    print('As strings possuem o mesmo comprimento!')
else:
    print('As strings não possuem o mesmo tamanho!')
    
if stringUm == stringDois:
    print('As strings possuem o mesmo conteúdo!')
else:
    print('As strings não possuem o mesmo conteúdo!')