def maior(*num):
    print('Analizando valores passados...')

    if num:
        maiorNum = max(num)

        for valor in num:
            print(f'{valor}', end=' ')

        print(f'= Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor de informado foi {maiorNum}')
        
    else:
        print('Foram informado 0 valores ao todo.')
        print('O maior valor informado foi 0.')

def linha():
    print('=-' * 25)

linha()
maior(2, 9, 4, 5, 6, 3)
linha()
maior(4, 2, 6, 7, 1)
linha()
maior(3, 6)
linha()
maior(5)
linha()
maior()
print()


