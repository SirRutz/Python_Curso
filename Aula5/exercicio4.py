# Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima: • idade média das mulheres • idade média dos homens • idade média do grupo

homem = []
mulher = []
tudo = []

for numero in range(10):
    
    sexo = input('Digite seu sexo(Masculino ou Feminino): ')
    idade = int(input('Digite sua idade: '))
    tudo.append(idade)
    

    if sexo == 'masculino':
        homem.append(idade)
    elif sexo == 'feminino':
        mulher.append(idade)

mediaMulher = (sum(mulher) / len(mulher))
mediaHomem = (sum(homem) / len(homem))
mediaGeral = (sum(tudo) /  len(tudo))

print('A idade média das mulheres é: {:.2f}'.format(mediaMulher))
print('A idade média dos homens é: {:.2f}'.format(mediaHomem))
print('A idade média de todos é: {:.2f}'.format(mediaGeral))


    

