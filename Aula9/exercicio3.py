# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso

def valorPagamento (valorPrestacao, dias):
    
    if dias == 0:
        return valorPrestacao
    
    elif dias >0:
        valor = valorPrestacao + (valorPrestacao * 0.03)
        resultado = valor + (dias * 0.001)
        return resultado

contador = 0
valorPrestacoesDia = 0

while True:
    dinheiro = float(input('Digite o valor original do produto (0 para sair): '))
    if dinheiro == 0:
        break
    elif dinheiro <0:
        print('Valor inválido!')
        break
    
    tempo = int(input('Digite o número de dias do atraso: '))
    if tempo <0:
        print('Valor inválido!')
        break
        
    contador += 1
        
    valorPrestacoesDia += valorPagamento (dinheiro, tempo)
    

print('Quantidade de prestações pagas:', contador,' Valor total pago: R$ {:.2f}'.format(valorPrestacoesDia))
    
    