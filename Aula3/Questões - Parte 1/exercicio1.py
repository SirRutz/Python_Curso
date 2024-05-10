#Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado(para ser aprovado a média deve ser no mínimo 6)

portugues = float(input('Digite sua nota de português: '))
matematica = float(input('Digite sua nota de matemática: '))

media = (portugues+matematica)/2

if media >=6:
    print('Parabéns! Você foi aprovado(a)')
else:
    print('Média baixa para a aprovação')
    