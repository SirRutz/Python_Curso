# Escreva um programa que solicite vários números ao usuário, sendo um de cada vez, possibilitando encerrar a entrada de dados informando zero. Adicione os números informados em uma lista e, ao final do programa, imprima a soma de todos os números, a multiplicação de todos os números, o maior e o menor número informado.

tudo = []

while True:
    num = int(input('Digite um numero inteiro (0 para sair): '))
    if num == 0:
        break
    tudo.append(num)

soma = sum(tudo)
print('A soma dos números presentes na lista é:',soma)

multi = 1
for num in tudo:
    multi *= num
print('A multiplicação dos números presentes nessa lista é: ',multi)

tudo.sort
print('O menor númreo da lista é:',tudo[0])
print('O maior número da lista é:',tudo[-1])

    
