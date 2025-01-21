#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar... dolar 6.10
real = float(input('\nValor a ser convertido(R$): '))
cotacao = float(input('Cotação atual do dolar($): ')) 
dolar = real / cotacao
print(f'Conversão do valor em dolar: {dolar:.2f}')