# Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média.


provaUm = (7.5 , 6.5 , 9.0 , 2.0, 5.5)
provaDois = (9.5, 1.0, 10.0, 6.0, 8.5)


mediaUm = sum(provaUm) / len(provaUm)
mediaDois = sum(provaDois) / len(provaDois)

print(f'A media da primeira prova é: {mediaUm}')
print(f'A media da segunda prova é: {mediaDois}')

if mediaUm > mediaDois:
    print('A primeira prova teve a melhor média da turma!')
elif mediaDois > mediaUm:
    print('A segunda prova teve a melhor média da turma!')
elif mediaUm == mediaDois:   
    print('As duas provas tiveram a mesma média!') 
