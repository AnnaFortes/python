cadastro = []
mulher = []
pessoaAcima = []
soma = 0

while True:
    pessoas = {}

    pessoas['nome'] = str(input('Nome: '))

    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]

        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoas['idade'] = int(input('Idade: '))

    soma += pessoas['idade']

    cadastro.append(pessoas)

    if pessoas['sexo'] == 'F':
        mulher.append(pessoas['nome'])
    
    while True:
        continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]

        if continuar in 'NS':
            break
        print('ERRO! Por favor, digite apenas N ou S.')

    if continuar == 'N':
        break

media = soma / len(cadastro)

for pessoa in cadastro:
    if pessoa['idade'] > media:
        pessoaAcima.append(pessoa)

print('=-' * 30)
print(cadastro)
print('=-' * 30)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {media:.1f} anos.')
print(f'- As mulheres cadastradas foram: {mulher}')
print('- Lista de pessoas que estão acima da média:')

for pessoa in pessoaAcima:
    print(f'\tnome = {pessoa["nome"]} ; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}')
    
print('<< ENCERRADO >>')
print()