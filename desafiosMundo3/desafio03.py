from random import randint
numTupla = ()
maior = menor = None

for num in range(5):
    numGerado = randint(0, 9)
    numTupla += (numGerado,)

    if maior is None or numGerado > maior:
        maior = numGerado

    if menor is None or numGerado < menor:
        menor = numGerado

print(f'Os valores sorteados foram: {numTupla}')
print(f'O maior valor sorteado foi : {maior}')
print(f'O menor valor sorteado foi: {menor}')


