altura = float(input('Digite a altura em centímetros: '))
comprimento = float(input('Digite o comprimento em centímetros: '))
largura = float(input('Digite a largura em centímetros: '))
volume = altura * comprimento * largura   
consumo = float(input('Digite o consumo médio diário de litros: '))
autonomia = volume / consumo


print('A capacidade total do reservatório é de', volume,'litros')
print('A autonomia do reservatório é de ',autonomia,'dias')

#  Consumo elevado, se a autonomia for menor que 2 dias; Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia maior que 7 dias.

if autonomia >7:
    print('Consumo reduzido')
elif autonomia <2:
    print('Consumo elevado')
elif autonomia <=7 >=5:
    print('Consumo moderado')