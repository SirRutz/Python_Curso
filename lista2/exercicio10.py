# Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.

ano = int(input('Digite um ano: '))

if ano % 400 == 0 or ano % 4 == 0:
    print(ano,'é ano bissexto!')
elif ano % 100 == 0:
    print(ano,'não é ano bissexto')
else:
    print(ano,'não é bissexto!')
    
