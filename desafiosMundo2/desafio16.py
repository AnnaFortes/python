#n - 1, é o termo que vc quer, nesse caso quero 10, poderia substituir o n por 10
print('=' * 25)
print('10 TERMOS DE UMA PA')
print('=' * 25)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for n in range(1, 11):
    pa = termo + (n - 1) * razao 
    print(f'{pa}', end=" -> ")
print('ACABOU')
