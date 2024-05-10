#  Dada uma tupla L de n valores inteiros, escreva um programa que remova os números pares da lista

numerosTupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuplaSemPares = ()

for numeros in numerosTupla:
    if numeros % 2 != 0:
        tuplaSemPares += (numeros,)
        
print(f'A tupla sem números pares é: {tuplaSemPares}')