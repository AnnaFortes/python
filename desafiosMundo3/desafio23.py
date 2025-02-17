cadastro = []
mulher = []
pessoaAcima = []
soma = 0

while True:
    pessoas = {}

    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))

    soma += pessoas['idade']

    cadastro.append(pessoas)

    if pessoas['sexo'] == 'F':
        mulher.append(pessoas['nome'])

    continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

media = soma / len(cadastro)

for p in cadastro:
    if p['idade'] > media:
        pessoaAcima.append(p)

print('=-' * 30)
print(cadastro)
print('=-' * 30)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: {mulher}')
print(f'- Lista de pessoas que estão acima da média: {pessoaAcima}')
print('<< ENCERRADO >>')
print()