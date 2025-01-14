#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dia pelos quais ele foi alugado. Calcule o preço, sabendo que o carro custa rs60 por dia e rs0.15 por km rodado
km = float(input('\nQuantos KM rodados: '))
dia = int(input('Quantos dia alugados: '))
total = (km * 0.15) + (dia * 60)
print(f'O total a pagar é R${total :.2f}\n')