# Escreva um programa em Python para encontrar o fatorial de qualquer número.


numero = int(input("Digite um número para calcular o fatorial: "))
resultado = 1

if numero < 0:
    print("Não é possível efetuar a conta")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for fatorial in range(1, numero + 1):
        resultado *= fatorial
    
    print(f"O fatorial de {numero} é {resultado}.")