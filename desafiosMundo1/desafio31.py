from datetime import date
ano = int(input('\nInforme um ano para saber se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year #vai pegar o ano atual
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'{ano} é um ano bissexto')
else: 
    print(f'{ano} não é um ano bissexto')