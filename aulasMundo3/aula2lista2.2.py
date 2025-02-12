galera = []
dados = []
totMaior = totMenor = 0 #só posso fazer isso com variavéis simples
for c in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) 
    dados.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totMenor += 1

print(f'Temos {totMaior} pessoas maiores de idade')
print(f'Temos {totMenor} pessoas menores de idade')
print()
