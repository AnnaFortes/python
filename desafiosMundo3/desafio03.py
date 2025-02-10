from random import randint
numTupla = ()

for num in range(5):
    numGerado = randint(0, 9)
    numTupla += (numGerado,)

print(f'Os valores sorteados foram: {numTupla}')
print(f'O maior valor sorteado foi : {max(numTupla)}')
print(f'O menor valor sorteado foi: {min(numTupla)}')
#max e min são métodos usados em TUPLAS, LISTAS, DICS ETC


