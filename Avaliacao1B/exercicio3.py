positivo = []
negativo = []

perguntaUm = input('Telefonou para a vítima? ').upper()
if perguntaUm == 'SIM':
    positivo.append(perguntaUm)
elif perguntaUm == 'NÃO':
    negativo.append(perguntaUm)

perguntaDois = input('Esteve no local do crime? ').upper()
if perguntaDois == 'SIM':
    positivo.append(perguntaDois)
elif perguntaDois == 'NÃO':
    negativo.append(perguntaDois)

perguntaTres = input('Mora perto da vítima? ').upper()
if perguntaTres == 'SIM':
    positivo.append(perguntaTres)
elif perguntaTres == 'NÃO':
    negativo.append(perguntaTres)

perguntaQuatro = input('Devia para a vítima? ').upper()
if perguntaQuatro == 'SIM':
    positivo.append(perguntaQuatro)
elif perguntaQuatro == 'NÃO':
    negativo.append(perguntaQuatro)

perguntaCinco = input('Ja trabalhou com a vítima? ').upper()
if perguntaCinco == 'SIM':
    positivo.append(perguntaCinco)
elif perguntaCinco == 'NÃO':
    negativo.append(perguntaCinco)


if len(positivo) == 2:
    print('Suspeita')
elif len(positivo) == 3 or len(positivo) == 4:
    print('Cúmplice')
elif len(positivo) == 5:
    print('Assassino')
else:
    print('Inocente')


