def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
""" SAÍDA: 
Recebi os valores (2, 1, 7) e são ao todo 3 números.
Recebi os valores (8, 0) e são ao todo 2 números.
Recebi os valores (4, 4, 7, 6, 2) e são ao todo 5 números.
"""