lista = []
listaInvertida = lista.reverse()

nota = float(input('Digite a nota: '))

while nota >0:
    lista.append(nota)
    
    if nota <0:
        break
    
    nota = float(input('Digite outra nota: '))
   
media = sum(lista) / len(lista)

notasAcima = []

for notas in lista:
    if notas > media:
        notasAcima.append(notas)
 
notasAbaixoSete = []

for notas in lista:
    if notas <7:
        notasAbaixoSete.append(notas)     

print(f'Foram lidos {len(lista)} valores')
print(f'Os valores informados foram: {lista}')
######
print(f'A soma dos valores foi {sum(lista)}')
print('A média dos valores foi: {:.2f}'.format(media))
print(f'Os valores acima da média foram: {notasAcima}')               
print(f'As notas abaixo de 7 foram: {len(notasAbaixoSete)}')
print('Obrigado por utilizar nosso programa!')
        
    

    
    


    
