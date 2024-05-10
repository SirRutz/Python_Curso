# Crie um programa para entrar com um número no formato CDU e imprimi-lo invertido: UDC. Por exemplo: 123 sairá 321. O número deverá ser armazenado em outra variável antes de ser impresso.

numero = int(input('Digite um número no formato CDU (Centena,Dezena,Unidade): '))

centena = (numero//100) 
dezena = ((numero%100) // 10) *10
unidade = (numero % 10) * 100

print(centena+dezena+unidade)
