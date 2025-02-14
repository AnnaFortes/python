matriz = []
soma = somaL = 0

for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}][{c}]: '))
        linha.append(valor)
    matriz.append(linha)

print('=-' * 30)

for linha in matriz:
    somaL += linha[-1] 
    for valor in linha:
        if valor % 2 == 0:
            soma += valor
        print(f'[{valor:^3}]', end=' ')
    print()

maior = max(matriz[1])

print('=-' * 30)
print(f'A soma entre todos é valores pares é de {soma}')
print(f'A soma entre os valores da 3° coluna é de {somaL}')
print(f'O maior valor da 2° linha é {maior}')
print() 

