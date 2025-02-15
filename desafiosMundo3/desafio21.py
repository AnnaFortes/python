from datetime import date

trabalho = {}

trabalho['nome'] = str(input('Nome: '))
trabalho['nascimento'] = int(input('Ano de nascimento: '))
trabalho['idade'] = date.today().year - trabalho['nascimento']
trabalho['carteiraCtps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalho['carteiraCtps'] != 0:
    trabalho['contratacao'] = int(input('Ano de contratação: '))
    trabalho['salario'] = float(input('Salário: '))
    trabalho['aposentadoria'] = (trabalho['contratacao'] + 35) - trabalho['nascimento']
    
print('=-' * 30)

if trabalho['carteiraCtps'] == 0 or trabalho['carteiraCtps'] != 0:
    print(f'Nome tem o valor {trabalho["nome"]}')
    print(f'Idade tem o valor {trabalho["idade"]}')
    print(f'CTPS tem o valor {trabalho["carteiraCtps"]}')

if trabalho['carteiraCtps'] != 0:
    print(f'Contratação tem o valor {trabalho["contratacao"]}')
    print(f'Salário tem o valor {trabalho["salario"]}')
    print(f'Aposentadoria tem o valor {trabalho["aposentadoria"]}')
    print()
