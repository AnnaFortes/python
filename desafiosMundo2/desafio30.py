continuar = 'S'
cont = 0
soma = 0
maior = None
menor = None

while continuar in 'Ss': 
    num = int(input('Digite um número: '))

    cont += 1    
    soma += num

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]

media = soma / cont

print(f'Você digitou {cont} números.')   
print(f'A média entre eles foi {media :.1f}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')
    