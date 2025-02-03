print('=-' * 15)
print(' ' * 6, 'TERMOS DE UMA PA')
print('=-' * 15)

termo = int(input('Primero termo: '))
razao = int(input('Razão: '))

cont = 0

while cont < 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM!')
    