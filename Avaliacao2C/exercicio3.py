veiculo = 0 
modelos = []
consumo = []

while len(modelos) <6:
    
    carros = input('Digite um modelo de um carro: ')
    modelos.append(carros)
    
    gasolina = float(input('Digite quantos Kms esse carro faz por litro: '))
    consumo.append(gasolina)
    
    if len(consumo) == 5:
        break
    
    
    
print('------------------------------------------')   
print(f'Veículo: {(veiculo +1)}')
print(f'Nome: {modelos[0]}')
print(f'Km por litro: {consumo[0]}')

print(f'Veículo: {(veiculo +2)}')
print(f'Nome: {modelos[1]}')
print(f'Km por litro: {consumo[1]}')

print(f'Veículo: {(veiculo +3)}')
print(f'Nome: {modelos[2]}')
print(f'Km por litro: {consumo[2]}')

print(f'Veículo: {(veiculo +4)}')
print(f'Nome: {modelos[3]}')
print(f'Km por litro: {consumo[3]}')

print(f'Veículo: {(veiculo +5)}')
print(f'Nome: {modelos[4]}')
print(f'Km por litro: {consumo[4]}')
print('------------------------------------------')

if max(consumo) == consumo[0]:
    print(f'Carro mais econômico: {modelos[0]}')
elif max(consumo) == consumo[1]:
    print(f'Carro mais econômico: {modelos[1]}')
elif max(consumo) == consumo[2]:
    print(f'Carro mais econômico: {modelos[2]}')
elif max(consumo) == consumo[3]:
    print(f'Carro mais econômico: {modelos[3]}')
elif max(consumo) == consumo[4]:
    print(f'Carro mais econômico: {modelos[4]}')

consumoMilPrimeiro = 1000 / consumo[0]
consumoMilSegundo = 1000 / consumo[1]
consumoMilTerceiro = 1000 / consumo[2]
consumoMilQuarto = 1000 / consumo[3]
consumoMilQuinto = 1000 / consumo[4]

precoGasolinaPrimeiro = (1000/consumo[0] * 2.25)
precoGasolinaSegundo = (1000/consumo[1] * 2.25)
precoGasolinaTerceiro = (1000/consumo[2] * 2.25)
precoGasolinaQuarto = (1000/consumo[3] * 2.25)
precoGasolinaQuinto = (1000/consumo[4] * 2.25)
    
print(modelos[0],'-', consumo[0],'- Consumo por litros: {:.1f}'.format(consumoMilPrimeiro),'- Preço: R$ {:.2f}'.format(precoGasolinaPrimeiro))
print(modelos[1],'-', consumo[1],'- Consumo por litros: {:.1f}'.format(consumoMilSegundo),'- Preço: R$ {:.2f}'.format(precoGasolinaSegundo))
print(modelos[2],'-', consumo[2],'- Consumo por litros: {:.1f}'.format(consumoMilTerceiro),'- Preço:R$ {:.2f}'.format(precoGasolinaTerceiro))
print(modelos[3],'-', consumo[3],'- Consumo por litros: {:.1f}'.format(consumoMilQuarto),'- Preço: R$ {:.2f}'.format(precoGasolinaQuarto))
print(modelos[4],'-', consumo[4],'- Consumo por litros: {:.1f}'.format(consumoMilQuinto),'- Preço: R$ {:.2f}'.format(precoGasolinaQuinto))