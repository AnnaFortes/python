menor = 0
maior = 0
for c in range(6):
    peso = float(input('Digite o peso (KG): '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O maior peso é {maior :.1f}')
print(f'O menor peso é {menor :.1f}')
