# Faça um programa que solicite ao usuário um número que ele queira treinar a tabuada. Você irá solicitar ao mesmo a resposta do cálculo do número informado multiplicado por 1, 2 até 10. A cada resposta você deverá validar e imprimir :”CORRETO” ou “QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X “, no lugar de ”X“ coloque o valor correto Ao final imprima “Total de acertos: y” e “Total de erros z”, onde “y“ deverá ser o total de acertos e “z“ o total de erros. Ao final da sequencia deve-se perguntar se deseja começar denovo.

correto = []
errado = []
tudo = [correto,errado]
mult = 1

num = int(input('Digite um número para treinar: '))

for resposta in range(10):
    resposta = int(input(f'Agora, digite esse numero multiplicado por {mult}: '))
    if resposta == (num*mult):
        print('Correto')
        correto.append(1)
    else:
        print(f'Que pena, você errou, o valor correto é {num*1}')
        errado.append(1)
    
    mult = mult+1
        
print(f'Total de acertos: {correto.count(1)} e Total de erros:{errado.count(1)}')