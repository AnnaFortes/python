from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    print(f'O alistamento é somente com 18 anos, ainda faltam {18 - idade} anos.\nSeu alistamento será em {nasc + 18}')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} anos! \nSeu alistamento foi em {nasc + 18}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
