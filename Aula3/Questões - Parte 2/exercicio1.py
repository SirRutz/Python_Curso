# Desenvolva um programa que recebe do usuário, o placar de um jogo de futebol (os gols de cada time) e informa se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

time1 = int(input('Insira o número de gols do primeiro time: '))
time2 = int(input('Insira o número de gols do segundo time: '))

if time1 > time2:
   print('Time 1 é o vencedor!!!')
elif time1 == time2:
    print('Empate')
else:
    print('Time 2 é o vencedor!!!')
