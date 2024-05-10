# Criar um algoritmo que, dado um número de conta corrente com três dígitos, retorne o seu dígito verificador, o qual é calculado da seguinte maneira:

numero = int(input('Digite um número no formato CDU (Centena,Dezena,Unidade): '))

#centena = numero // 100
#dezena = ((numero%100) // 10) 
#unidade = numero % 10

centenaInvertida = (numero//100) 
dezenaInvertida = ((numero%100) // 10) *10
unidadeInvertida = (numero % 10) * 100

numeroInvertido = (centenaInvertida + dezenaInvertida +unidadeInvertida)
soma = numero + numeroInvertido

centena = soma // 100
dezena = ((soma%100) // 10) 
unidade = soma % 10

mult = centena + (dezena * 2) + (unidade *3)

digito = str(mult) [-1]

print('Digito verificador:',digito)

