nome = input('Digite o seu nome: ')

saltoUm = float(input('Digite a distância alcançada no primeiro salto: '))
saltoDois = float(input('Digite a distância alcançada no segundo salto: '))
saltoTres = float(input('Digite a distância alcançada no terceiro salto: '))
saltoQuatro = float(input('Digite a distância alcançada no quarto salto: '))
saltoCinco = float(input('Digite a distância alcançada no quinto salto: '))

media = (saltoUm + saltoDois + saltoTres + saltoQuatro + saltoCinco) / 5

print(f'Atleta: {nome}')
print(f'Primeiro Salto: {saltoUm}')
print(f'Segundo Salto: {saltoDois}')
print(f'Terceiro Salto: {saltoTres}')
print(f'Quarto Salto: {saltoQuatro}')
print(f'Quinto Salto: {saltoCinco}')
print('Resultado final: {:.2f}'.format(media))


