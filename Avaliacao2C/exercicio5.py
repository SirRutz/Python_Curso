aluno = {}
mediaGeral = []

while aluno != 0:
    
    aluno['nome'] = str(input('Nome: '))
     
    if aluno['nome'] == ' ':
     break
    
    aluno['nota1'] = float(input(f"Nota um de {aluno['nome']}: "))
    aluno['nota2'] = float(input(f"Nota dois de {aluno['nome']}: "))
    
    aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    mediaGeral.append(aluno['media'])
    
    

    print('Média:', aluno['media'])

print('A maior média foi:', max(mediaGeral))

