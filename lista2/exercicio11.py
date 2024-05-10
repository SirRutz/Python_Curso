# . Leia uma data e determine se ela e válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos. A ordem de leitura e impressão dos dados é: dia, mês, ano

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes >= 1 and mes <= 12:
    if mes == 2:  
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:  
            if dia >= 1 and dia <= 29:
                print(dia,'/',mes,'/',ano,'é uma data válida!')
            else:
                print(dia,'/',mes,'/',ano,'não é uma data válida')
        else:
            if dia >= 1 and dia <= 28:
                print(dia,'/',mes,'/',ano,'é uma data válida!')
            else:
                print(dia,'/',mes,'/',ano,'não é uma data válida')
    elif mes in [1, 3, 5, 7, 8, 10, 12]:  
        if dia >= 1 and dia <= 31:
            print(dia,'/',mes,'/',ano,'é uma data válida!')
        else:
            print(dia,'/', mes,'/',ano,'não é uma data válida')
    else:  
        if dia >= 1 and dia <= 30:
            print(dia,'/',mes, '/',ano,'é uma data válida!')
        else:
            print(dia,'/',mes,'/',ano,'não é uma data válida')
else:
    print(dia,'/',mes,'/',ano,'não é uma data válida')

