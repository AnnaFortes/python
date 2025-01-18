#ler o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
cidade = str(input('Digite uma cidade: ')).strip().lower()
print('santo' in cidade[:6])