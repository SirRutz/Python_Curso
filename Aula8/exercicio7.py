# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado

import random

lista = ('MAÇÃ','BANANA','LARANJA','MELANCIA','UVA')
elementoAleatorio = random.choice(lista)
contador = 0

for chute in range(6):
  chute = input('Digite seu chute para a palavra (dica: é uma fruta): ')
  chuteMaiusculo = chute.upper()
  
  if contador >6:
      break
  

  if chuteMaiusculo == elementoAleatorio:
    print('Parabéns, você acertou!')
    break
  
  elif chuteMaiusculo != elementoAleatorio:
    contador += 1
    
    if(6 - contador) == 1:
        print(f'Que pena, você errou, você tem mais 1 chance!') 
    elif (6 - contador) == 0:
        print('Que pena, você errou todas as tentativas!')
    else:
        print(f'Que pena, você errou, você tem mais {6 - contador} chances!')