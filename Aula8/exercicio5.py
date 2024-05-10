# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte: a) quantos espaços em branco existem na frase. b) quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma frase: ')
fraseMinuscula = frase.lower()
vogais = 'aãâáàéêèiìíoôõu'
contador = 0

print('A frase tem',frase.count(' '),'espaços em branco')

for letras in fraseMinuscula:
    if letras in vogais:
       contador += 1
    
print(f'Existem {contador} vogais na frase')