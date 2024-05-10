# Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de um produto e imprima o novo valor tendo em vista que o desconto foi de 9%.

valor = float(input('Insira o valor original do produto: '))

print('Com o desconto, o produto custará:', valor - valor*(9/100))