# . Escreva um programa que leia o código de um aluno e suas três notas. Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e uma mensagem “APROVADO” se a média for maior ou igual a 5 e “REPROVADO" se a média for menor que 5.

codigo = int(input('Digite o seu código: '))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

if nota1 > nota2 and nota1 > nota3:
   media1 = ((4*nota1) + (3*nota2) + (3*nota3)) / 10
   print('código:',codigo, 'nota1:',nota1, 'nota2:',nota2, 'nota3:',nota3,'média:{:.2f}'.format(media1))
   if media1 <5:
      print('REPROVADO')
   else:
      print('APROVADO')
elif nota2 > nota1 and nota2 > nota3:
   media2 = ((nota2 * 4) + (nota1 * 3) + (nota3 * 3)) / 10
   print('código:',codigo, 'nota1:',nota1, 'nota2:',nota2, 'nota3:',nota3,'média:{:.2f}'.format(media2))
   if media2 <5:
      print('REPROVADO')
   else:
      print('APROVADO')
elif nota3 > nota1 and nota3 > nota1:
   media3 = ((nota3 * 4) + (nota2 * 3) + (nota1 * 3)) / 10
   print('código:',codigo, 'nota1:',nota1, 'nota2:',nota2, 'nota3:',nota3,'média:{:.2f}'.format(media3))
   if media3 <5:
      print('REPROVADO')
   else:
      print('APROVADO')
    