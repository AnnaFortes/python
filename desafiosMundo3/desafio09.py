valores = []

for c in range(5): 
    num = int(input('Digite um valor: '))

    if not valores or num > valores[-1]: #Se a lista estiver vazia ou se num for maior que o último valo
        valores.append(num) 
        print('Adicionado no final da lista...')
    else:
        pos = 0

        while pos < len(valores) and valores[pos] < num: 
            pos += 1
        valores.insert(pos, num) 
        print(f'Adicionando na posição {pos} da lista...')

print('=-' * 20)
print(f'Os valores digitados em ordem foram {valores}')
print()
        