aluno = {}
boletim = []

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']} : '))

boletim.append(aluno)

print('-' * 25)
print(f'Nome é igual a {boletim[0]['nome']}')
print(f'A média é igual a {boletim[0]['media']:.1f}')

if boletim[0]['media'] < 7 and boletim[0]['media'] > 6:
    print('Situação atual em Recuperação!')
elif boletim[0]['media'] < 6:
    print('Situação atual Reprovado!')
else:
    print('Situação atual Aprovado!')
print()