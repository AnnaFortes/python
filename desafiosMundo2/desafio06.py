from datetime import date
nasc = int(input('\nDigite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('ATLETA MIRIN')
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JUNIOR')
elif idade <= 25:
    print('ATLETA SENIOR')
else:
    print('ATLETA MASTER')
