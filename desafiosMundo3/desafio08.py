num = []

while True:
    novoNum = int(input('Digite um valor: '))

    if novoNum in num: 
        print('Valor duplicado! Não vou adicionar...')
    else: 
        num.append(novoNum)
        print('Valor adicionado com sucesso!')
    
    continuar = str(input('Gostaria de continuar: [S/N] ')).upper().split()[0]

    if continuar == 'N':
        print('=-' * 20)
        break

print(f'Você digitou os valores {sorted(num)}') 

