# Faça um programa que crie uma tupla com o que você quiser dentro e depois altere o último elemento para o número 3.

lista = []

while lista !=0:
   
   resposta = int(input('Digite um numero (0 para sair): '))
   if resposta != 0:
    lista.append(resposta)
   
   if resposta == 0:
       break

del lista[-1]
lista.append(3)
print(f'A tupla com o último elemento substituido por três é: {tuple(lista)}')