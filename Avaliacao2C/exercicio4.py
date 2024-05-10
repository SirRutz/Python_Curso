mouses = 0
necessitaEsfera = 0
necessitaLimpeza = 0
necessitaCabo= 0
quebrado = 0


for mouses in range(200):
    
  identificacao = int(input('Digite o número de identificação do mouse: '))
  defeito = int(input('Descreva o erro da seguinte forma (1 - necessita de esfera,  2 - necessita de limpeza,  3 - necessita troca do cabo ou conector,  4 - quebrado ou inutilizado): '))

    
  if defeito == 0 or defeito <0 or defeito >4:
        break
    
  if defeito == 1:
     necessitaEsfera += 1
     
  if defeito == 2:
        necessitaLimpeza += 1
        
  if defeito == 3:
        necessitaCabo =+ 1
        
  if defeito == 4:
        quebrado += 1
  
  mouses += 1
        
print(f'Necessita da esfera: {necessitaEsfera}')
print(f'Necessita de limpeza: {necessitaLimpeza}')
print(f'Necessita troca do cabo ou conector: {necessitaCabo}')
print(f'Quebrado ou inutilizado: {quebrado}')

######