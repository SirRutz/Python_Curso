# Crie um programa para entrar com um número no formado CDU (centena, dezena e unidade) e exibi-lo de acordo com a seguinte saída:

numero = int(input('Digite um número no formato CDU (Centena,Dezena,Unidade): '))

print('A centena desse número é: ', numero//100)
print('A dezena desse número é: ', (numero%100)//10)
print('A unidade desse número é: ', numero % 10)
