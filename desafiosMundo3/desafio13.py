pessoas = [] 
maiorNome = []
menorNome = []
maior = menor = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso KG: '))

    pessoas.append([nome, peso])

    if peso > maior:
        maior = peso
        maiorNome = [nome]
    elif peso == maior:
        maiorNome.append(nome)

    if peso < menor:
        menor = peso
        menorNome = [nome]
    elif peso == menor:
        menorNome.append(nome)
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        print('=-' * 30)
        break

print(f'Ao total temos {len(pessoas)} pessoas')

print(f'O maior peso foi de {', '.join(maiorNome)}. Peso de {maior}')
print(f'O menor peso foi de {', '.join(menorNome)}. Peso de {menor}')