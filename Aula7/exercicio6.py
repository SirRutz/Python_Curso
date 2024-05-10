# Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).

semana = {}
semana2 = {'Segunda':['Matemática','Inglês'], 'Terça':['Artes','Matemática'], 'Quarta':['Português','História'], 'Quinta':['Química','Biologia'], 'Sexta':['Física','Português']}

semana.update(semana2)
print(semana)