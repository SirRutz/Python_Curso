listaAltura = []
listaTrezeAnos = []

idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

for altura in range(30):
 listaAltura.append(altura)

 media = sum(listaAltura) / len(listaAltura)

 if idade >13:
    if altura < media:
        listaTrezeAnos.append(altura)
    
 
print(f'O total de {listaTrezeAnos.count} alunos com 13 anos possuem altura inferior a média da turma!')


    
    

