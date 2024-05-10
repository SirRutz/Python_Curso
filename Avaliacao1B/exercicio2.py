
meses = []

temperaturaJaneiro = float(input('Digite a temperatura média de Janeiro: '))
meses.append(temperaturaJaneiro)

temperaturaFevereiro = float(input('Digite a temperatura média de Fevereiro: '))
meses.append(temperaturaFevereiro)

temperaturaMarco = float(input('Digite a temperatura média de Março: '))
meses.append(temperaturaMarco)

temperaturaAbril = float(input('Digite a temperatura média de Abril: '))
meses.append(temperaturaAbril)

temperaturaMaio = float(input('Digite a temperatura média de Maio: '))
meses.append(temperaturaMaio)

temperaturaJunho= float(input('Digite a temperatura média de Junho: '))
meses.append(temperaturaJunho)

temperaturaJulho = float(input('Digite a temperatura média de Julho: '))
meses.append(temperaturaJulho)

temperaturaAgosto = float(input('Digite a temperatura média de Agosto: '))
meses.append(temperaturaAgosto)

temperaturaSetembro = float(input('Digite a temperatura média de Setembro: '))
meses.append(temperaturaSetembro)

temperaturaOutubro = float(input('Digite a temperatura média de Outubro: '))
meses.append(temperaturaOutubro)

temperaturaNovembro = float(input('Digite a temperatura média de Novembro: '))
meses.append(temperaturaNovembro)

temperaturaDezembro = float(input('Digite a temperatura média de Dezembro: '))
meses.append(temperaturaDezembro)

mediaAnual = sum(meses) / 12
print('A temperatura média anual foi de: {:.2f}'.format(mediaAnual) )

temperaturaAlta = []

if meses[0] > mediaAnual:
    temperaturaAlta.append(f'Janeiro: {temperaturaJaneiro}')
    
if meses[1] > mediaAnual:
    temperaturaAlta.append(f'Fevereiro: {temperaturaFevereiro}')

if meses[2] > mediaAnual:
    temperaturaAlta.append(f'Março: {temperaturaMarco}')
    
if meses[3] > mediaAnual:
    temperaturaAlta.append(f'Abril: {temperaturaAbril}')

if meses[4] > mediaAnual:
    temperaturaAlta.append(f'Maio: {temperaturaMaio}')

if meses[5] > mediaAnual:
    temperaturaAlta.append(f'Junho: {temperaturaJunho}')

if meses[6] > mediaAnual:
    temperaturaAlta.append(f'Julho: {temperaturaJulho}')

if meses[7] > mediaAnual:
    temperaturaAlta.append(f'Agosto: {temperaturaAgosto}')

if meses[8] > mediaAnual:
    temperaturaAlta.append(f'Setembro: {temperaturaSetembro}')

if meses[9] > mediaAnual:
    temperaturaAlta.append(f'Outubro: {temperaturaOutubro}')

if meses[10] > mediaAnual:
    temperaturaAlta.append(f'Novembro: {temperaturaNovembro}')

if meses[11] > mediaAnual:
    temperaturaAlta.append(f'Dezembro: {temperaturaDezembro}')
    
print(f'Os meses que ultrapassaram a média anual foram: {temperaturaAlta}')






    