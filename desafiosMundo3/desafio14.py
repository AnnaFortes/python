listaNum = []
par = []
impar = []

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° valor: '))

    listaNum.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print('=-' * 25)   
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')


