somaIdade = 0
velho = 0
nomeVelho = ''
mulher21 = 0
for c in range(5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).lower()

    somaIdade += idade
    
    if sexo == 'masculino':
        if idade > velho:
            velho = idade
            nomeVelho = nome
    elif sexo == 'feminino':
        if idade < 21:
            mulher21 += 1
mediaIdade = somaIdade / 5            
print(f'A média da idade das pessoas é de {mediaIdade :.1f} anos.')
print(f'O homem mais velho é {nomeVelho} e tem {velho} anos')
print(f'No total {mulher21} mulheres são menores de 21 anos')
