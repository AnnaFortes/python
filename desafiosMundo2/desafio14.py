tab = int(input('Qual tabuada você gostaria de descobrir? '))
print('=-' * 10)
print(f'TABUADA DO {tab}')
print('=-' * 10)
for c in range(1, 11):
    r = tab * c
    print(f'{tab} x {c} = {r}')