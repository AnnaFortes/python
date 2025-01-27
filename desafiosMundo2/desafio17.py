num = int(input('Digite um número: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[32m', end=" ")
        tot += 1 
    else:
        print('\033[33m', end=" ")
    print(f'{n}', end=" ")
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
