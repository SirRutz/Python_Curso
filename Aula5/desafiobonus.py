# Faça um programa que solicite ao usuário um número que ele queira treinar a tabuada. Você irá solicitar ao mesmo a resposta do cálculo do número informado multiplicado por 1, 2 até 10. A cada resposta você deverá validar e imprimir :”CORRETO” ou “QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X “, no lugar de ”X“ coloque o valor correto Ao final imprima “Total de acertos: y” e “Total de erros z”, onde “y“ deverá ser o total de acertos e “z“ o total de erros.

correto = []
errado = []

num = int(input('Digite um número para treinar: '))

mult1 = num
mult2 = num*2
mult3 = num*3
mult4 = num*4
mult5 = num*5
mult6 = num*6
mult7 = num*7
mult8 = num*8
mult9 = num*9
mult10 = num*10

resposta1 = int(input('Digite esse número multiplicado por 1: '))
if resposta1 == mult1:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult1}')
    
resposta2 = int(input('Digite esse número multiplicado por 2: '))
if resposta2 == mult2:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult2}')
resposta3 = int(input('Digite esse número multiplicado por 3: '))
if resposta3 == mult3:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult3}')
resposta4 = int(input('Digite esse número multiplicado por 4: '))
if resposta4 == mult4:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult4}')
resposta5 = int(input('Digite esse número multiplicado por 5: '))
if resposta5 == mult5:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult5}')
resposta6 = int(input('Digite esse número multiplicado por 6: '))
if resposta6 == mult6:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult6}')
resposta7 = int(input('Digite esse número multiplicado por 7: '))
if resposta7 == mult7:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult7}')
resposta8 = int(input('Digite esse número multiplicado por 8: '))
if resposta8 == mult8:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult8}')
resposta9 = int(input('Digite esse número multiplicado por 9: '))
if resposta9 == mult9:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult9}')
resposta10 = int(input('Digite esse número multiplicado por 10: '))
if resposta10 == mult10:
    correto.append(1)
    print('Correto!')
else:
    errado.append(1)
    print(f'Que pena, você errou, o valor correto é {mult10}')
    
print(f'Total de acertos: {correto.count(1)} e Total de erros: {errado.count(1)}')