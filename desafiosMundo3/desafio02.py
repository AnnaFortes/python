brasileirao = ((1, 'Botafogo'), (2, 'Palmeiras'), (3, 'Flamengo'), (4, 'Fortaleza'), (5, 'Internacional'), (6, 'São Paulo'), (7, 'Corinthians'), (8, 'Bahia'), (9, 'Cruzeiro'), (10, 'Vasco'), (11, 'Vitória'), (12, 'Atlético-MG'), (13, 'Fluminense'), (14, 'Grêmio'), (15, 'Chapecoense'), (16, 'Red Bull Bragantino'), (17, 'Atético-PR'), (18, 'Criciúma'), (19, 'Atlético-GO'), (20, 'Cuiabá'))

print(f'Lista de times: {brasileirao}')

print('=-' * 15)

print(f'Os cinco primeiros colocados do Brasileirão são: ', end='')

for cont in range(5):
    print(f'{brasileirao[cont][1]}')

print('=-' * 15)

print(f'\nOs últimos quatro colocados são: ', end='')

for cont in range(-4, 0):
    print(f'{brasileirao[cont][1]}')

print('=-' * 15)

print(f'Times em ordem alfabética: {sorted(brasileirao)}')

print('=-' * 15)

for i in range(len(brasileirao)):
    if brasileirao[i][1] == 'Chapecoense':
        print(f'A Chapecoense está na posição {brasileirao[i][0]}')

print()

 

