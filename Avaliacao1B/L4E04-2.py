numero = int(input('Digite um número inteiro(0 para sair): '))
listaPares = []

while numero != 0:
    numero = int(input('Digite um número inteiro(0 para sair): '))
    
    if numero % 2 == 0:
        listaPares.append(numero)
    
    if numero == 0:
        break

print(f'A soma dos números pares digitados é igual a: {sum(listaPares)}')