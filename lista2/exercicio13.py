idade = int(input('Digite sua idade: '))
servico = int(input('Digite quantos anos voce trabalhou: '))

if idade >= 65:
    print('pode se aposentar!')
elif servico >= 30:
    print('pode se aposentar!')
elif idade >=60 and servico >=25:
    print('pode se aposentar!')
else:
    print('não pode se aposentar!')