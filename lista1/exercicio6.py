# Sabendo-se que 100 quilowatts de energia custa um sétimo de salário mínimo, fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência, calcule e imprima:-(O valor em reais de cada quilowatt; o valor em reais a ser pago; o novo valor a ser pago por essa residência com um desconto de 10%.)

salario = float(input('Digite seu salário: '))
quilowatt = float(input('Digite a quantidade de quilowatts utilizada: '))

valorQuilowatt = salario /700
valorTotal = valorQuilowatt * quilowatt
valorDesconto = valorTotal - (valorTotal * 0.1)

print('valor do quilowatt R${:.2f}'.format(valorQuilowatt))
print('Valor a ser pago R${:.2f}'.format(valorTotal))
print('Valor a ser pago, com desconto R${:.2f}'.format(valorDesconto))