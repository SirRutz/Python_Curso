# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    porcentagem = taxaImposto / 100
    resultado = custo + (custo * porcentagem)
    return resultado

taxa = float(input('Digite a porcentagem de imposto para ser aplicada: '))
custo = float(input('Digite o custo original do produto: '))
print('O valor do produto após imposto é: {:.2f}'.format(somaImposto(taxa , custo)))
