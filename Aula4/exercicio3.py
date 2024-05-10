# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. Adicione os números em uma lista, crie uma outra lista contendo os números sem repetição e uma outra contendo os números que se repetem na primeira lista.

numeros_sem_repeticao = []
numeros_com_repeticao = []
tudo = []

while True:
    num = int(input('Digite um numero (0 para sair): '))
    if num == 0:
        break
    tudo.append(num)

for num in tudo:
    if tudo.count(num) == 1 and num not in numeros_sem_repeticao:
      numeros_sem_repeticao.append(num)
    elif tudo.count(num) != 1 and num not in numeros_com_repeticao:
      numeros_com_repeticao.append(num)
     
print(f"Numeros informados: {tudo}")
print(f"Numeros sem repetição: {numeros_sem_repeticao}")
print(f"Numeros com repetição: {numeros_com_repeticao}")