salarioBruto = []
salariosSomados = []
abono = []
abonoCemContagem = []

while salariosSomados != 0:
    salario = float(input('Digite seu salário bruto de dezembro: '))
    if salario >0:
     salarioBruto.append(salario)
    
    
    if salario == 0 or salario <0:
     break
    
    if salario <1000:
        salarioMenor = salario + 100
        salariosSomados.append(salarioMenor)
        abono.append(100)
        abonoCemContagem.append(1)
        
    if salario >=1000:
        salarioMaior = salario + (salario * 0.2)
        salariosSomados.append(salarioMaior)
        abono.append(salario * 0.2)
        
print(f'Salarios brutos e abono:')
for numeros in salarioBruto:
    if numeros <1000:
        print(f'R$ {numeros} - R$ 100.00' )
    elif numeros >=1000:
        print(f'R$ {numeros} - R$ {(numeros * 0.2)}')
        
print(f'Total de funcionarios processados: {len(salarioBruto)}')
print(f'Total gasto com abono: {sum(abono)}')
print(f'Valor mínimo pago a {len(abonoCemContagem)} colaboladores')
print(f'Maior valor pago com abono: R$ {max(abono)}')


    
    