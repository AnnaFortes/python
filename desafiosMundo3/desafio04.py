numTupla = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o útimo número: '))
    )

print(f'Você digitou os valores {numTupla}')

print(f'O valor 9 apareceu {numTupla.count(9)} vezes')

if 3 in numTupla:
    print(f'O número 3 apareceu na {numTupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram: ', end='')
temPar = False

for c in numTupla:
    if c % 2 == 0:
        print(c)
        temPar = True 
        
if not temPar:
    print('Nenhum')
else:
    print()