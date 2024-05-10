# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

dia = int(input('Digite o dia em que você nasceu: '))
mes = int(input('Digite o mes em que você nasceu: '))
ano = int(input('Digite o ano em que você nasceu: '))

if mes == 1:
    print(f'{dia}/Janeiro/{ano}')
elif mes == 2:
    print(f'{dia}/Fevereiro/{ano}')
elif mes == 3:
    print(f'{dia}/Março/{ano}')
elif mes == 4:
    print(f'{dia}/Abril/{ano}')
elif mes == 5:
    print(f'{dia}/Maio/{ano}')
elif mes == 6:
    print(f'{dia}/Junho/{ano}')
elif mes == 7:
    print(f'{dia}/Julho/{ano}')
elif mes == 8:
    print(f'{dia}/Agosto/{ano}')
elif mes == 9:
    print(f'{dia}/Setembro/{ano}')
elif mes == 10:
    print(f'{dia}/Outubro/{ano}')
elif mes == 11:
    print(f'{dia}/Novembro/{ano}')
elif mes == 12:
    print(f'{dia}/Dezembro/{ano}')
else:
    print('Mês inválido!')
