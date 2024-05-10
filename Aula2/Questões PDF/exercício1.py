# Dado a nota das provas P1, P2 e P3, calcular a média (aritmética) das notas do aluno.

matematica = int(input('Digite sua nota de matemática: '))
portugues = int(input('Digite sua nota de português: '))
ingles = int(input('Digite sua nota de inglês: '))

media = (matematica + portugues + ingles)/3
print('A média de suas notas é:', media)