#ler um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
num = input('Digite um número de 0 a 9999: ')

print(f'Unidade: {num[:1]}')
print(f'Dezena: {num[:2]}')
print(f'Centena: {num[:3]}')
print(f'Milhar: {num[:4]}')