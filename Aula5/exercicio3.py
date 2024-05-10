# Faça um programa em linguagem Python que recebe a temperatura de z cliente e imprima a mensagem de se a temperatura esta normal (menor que 37,2 C) ou está em estado febril (37,3 C a 38 C ) ou com febre (38 C a 39 C) e com febre alta(acima 39 C). No final mostre a quantidade de pessoas analisadas e a média de temperatura.

lista = []

temperatura = float(input('Digite sua temperatura (0 para sair): '))

while temperatura != 0:
    lista.append(temperatura)
    if temperatura <37.2:
        print('Temperatura normal')
    elif temperatura <38 >37.2:
        print('Estado febril')
    elif temperatura <39 >38:
        print('Febre')
    elif temperatura >39:
        print('Febre alta')

    temperatura = float(input('Digite outra temperatura(0 para sair): '))

print (f'Quantidade de pessoas analisadas: {len(lista)}')

media = (sum(lista) / len(lista))
print(f'A media de temperatura foi: {media}')

   



