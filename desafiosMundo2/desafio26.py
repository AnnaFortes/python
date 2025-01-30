print('=-' * 15)
print(' ' * 6, 'TERMOS DE UMA PA')
print('=-' * 15)

termo = int(input('Primero termo: '))
razao = int(input('Razão: '))
n = int(input('Digite o número de termos: '))

cont = 0

while cont < n:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM!')
    