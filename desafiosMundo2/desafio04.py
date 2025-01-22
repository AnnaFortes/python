from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    falta = 18 - idade
    print(f'O alistamento é somente com 18 anos, ainda faltam {falta} anos.')
elif idade == 18:
    print('Você está em idade de se alistar!')
elif idade > 18:
    print('Você já passou da idade para se alistar!')
