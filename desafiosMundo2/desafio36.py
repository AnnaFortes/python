contN1 = contN2 = contN3 = contN4 = 0

print('=' * 35)
print('BANCO CEV'.center(35))
print('=' * 35)

valor = int(input('Valor a ser sacado R$'))

nota1 = 50
nota2 = 20
nota3 = 10
nota4 = 1

while valor >= nota1:
    valor -= nota1
    contN1 += 1

while valor >= nota2:
    valor -= nota2
    contN2 += 1

while valor >= nota3:
    valor -= nota3 
    contN3 += 1
    
while valor >= nota4:
    valor -= nota4 
    contN4 += 1

print(f'Total de {contN1} notas de R$50')
print(f'Total de {contN2} notas de R$20')
print(f'Total de {contN3} notas de R$10')
print(f'Total de {contN4} notas de R$1')
print('=' * 35)
print('Volte sempre ao banco CEV! Tenha um bom dia!')


