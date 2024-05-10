# Solicite ao usuário o valor do salário atual (numérico com decimais), em seguida, solicite o percentual de aumento (numérico com decimais) e imprima o valor do salário atualizado

salario = float(input('Digite seu salário atual: '))
percentual = float(input('Digite o percentual de aumento; '))

aumento = salario + (salario*(percentual/100))

print('O seu salário atual é:', aumento)