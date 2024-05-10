lista = []

contadorWindows = 0
contadorUnix = 0
contadorLinux = 0
contadorNetware = 0
contadorMacOS = 0
contadorOutro = 0

while lista != 0:
 
    votos = int(input('Digite seu voto (1 - Windows, 2 - Unix, 3 - Linux, 4 - Netware, 5 - MacOS, 6 - Outro): '))
    if votos >0 and votos <7:
     lista.append(votos)
    
    if votos ==0 or votos >6 or votos <0:
        break
   
    if votos == 1:
        contadorWindows += 1
    
    if votos == 2:
        contadorUnix += 1
    
    if votos == 3:
        contadorLinux += 1
    
    if votos == 4:
        contadorNetware += 1
        
    if votos == 5:
        contadorMacOS += 1
        
    if votos == 6:
        contadorOutro += 1
 
porcentagemWindows = (contadorWindows * 100) / sum(lista)
porcentagemUnix = (contadorUnix * 100) / sum(lista)
porcentagemLinux = (contadorLinux * 100) / sum(lista)
porcentagemNetware = (contadorNetware * 100) / sum(lista)
porcentagemMacOS = (contadorMacOS * 100) / sum(lista)
porcentagemOutro = (contadorOutro * 100) / sum(lista)


print(f'Sistema operacional, Votos, e %')         
print(f'Windows Server: {contadorWindows} / {porcentagemWindows}')
print(f'Unix: {contadorUnix} / {porcentagemUnix}')
print(f'Linux: {contadorLinux} / {porcentagemLinux}')            
print(f'Netware: {contadorNetware} / {porcentagemNetware}')            
print(f'MacOS: {contadorMacOS} / {porcentagemMacOS}')
print(f'Outro: {contadorOutro} / {porcentagemOutro}')
print(f'Total: {len(lista)}')





            