somaIdade = 0
velho = 0
nomeVelho = ''
mulher21 = 0
for c in range(1, 5):
    print('-'*5, f'{c}º PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    somaIdade += idade
    
    if sexo == 'm':
        if idade > velho:
            velho = idade
            nomeVelho = nome
    elif sexo == 'f':
        if idade < 21:
            mulher21 += 1
mediaIdade = somaIdade / 4           
print(f'A média da idade das pessoas é de {mediaIdade :.1f} anos.')
print(f'O homem mais velho é o {nomeVelho} e tem {velho} anos')
print(f'No total {mulher21} mulheres são menores de 21 anos')
