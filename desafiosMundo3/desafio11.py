lista = []
listaPar = []
listaImpar = []

while True:
    num = int(input('Digite um valor: '))

    lista.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

    continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        print('=-' * 20)
        break

print(f'Lista completa: {lista}')
print(f'Lista de pares: {listaPar}')
print(f'Lista de ímpares: {listaImpar}')
print()
    