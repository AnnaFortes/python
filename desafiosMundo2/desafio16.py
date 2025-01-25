termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for n in range(1, 11):
    pa = termo + (n - 1) * razao
    print(f'Termo{n}: {pa}')

