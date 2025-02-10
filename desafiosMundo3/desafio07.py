valores = []

for chave in range(5): 
    valor = int(input(f'Digite um valor para a posição {chave}: '))
    valores.append(valor)

print('=-' * 25)

print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

posMaior = []
posMenor = []

for p, v in enumerate(valores):
    if v == maior: 
        posMaior.append(p)
    if v == menor:
        posMenor.append(p)

print(f'O menor valor digitado foi {menor} na posição {posMenor}')

print(f'O maior valor digitado foi {maior} na posição {posMaior}')

print()
    
