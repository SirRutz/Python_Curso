# Criar um algoritmo que leia a quantidade de fitas que uma locadora de vídeo possui e o valor que ela cobra por cada aluguel, mostrando as informações pedidas a seguir: (a) Sabendo que um terço das fitas são alugadas por mês, exiba o faturamento anual da locadora; (b) Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel. Sabendo que um décimo das fitas alugadas no mês é devolvido com atraso, calcule o valor ganho com multas por mês; (c) Sabendo ainda que 2% das fitas se estragam ao longo do ano, e um décimo do total é comprado para reposição, exiba a quantidade de fitas que a locadora terá no final do ano.

fitas = int(input('Insira a quantidade de fitas que possui: '))
aluguel = float(input('Digite o valor do aluguel de suas fitas: '))

fitasAnual = ((fitas/3) * aluguel) * 12

fitasAtrasadas = (((fitas/10) * aluguel) * 0.1)

fitasTotais = (fitas - (fitas * 0.02)) + (fitas/10)

print ('Faturamento anual: R$',fitasAnual)
print('Valor multa mental R$',fitasAtrasadas)
print('total de fitas ao final de um ano:',fitasTotais)


