# Escreva um programa que solicite várias palavras ao usuário, sendo uma de cada vez, possibilitando encerrar a entrada de dados informando zero. Adicione as palavras informadas em uma lista. Após o usuário informar “0” (zero), solicite a palavra que ele deseja contar. Desta forma, o programa deverá contar as ocorrências daquela palavra. Ao final imprima o resultado.

tudo = []

while True:
    palavra = str(input('Digite uma palavra (0 para sair): '))
    if palavra == '0':
        break
    tudo.append(palavra)
    
ocorrencia = input('Digite a palavra que deseja ver a repetição: ')
qnt = tudo.count(ocorrencia)
print('Temos',qnt,'ocorrências de',ocorrencia)