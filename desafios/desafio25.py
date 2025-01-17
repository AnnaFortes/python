#leia o nome completo da pessoa, mostre o primeiro e o ultimo nome separadamente, ex: ana maria de souza, primeiro: ana, ultimo: souza
nome = input('\nDigite seu nome completo: ').lower()
nomeS = nome.split()
print(f'Nome completo: {nome}')
print(f'Primeiro nome: {nomeS[0]}')
print
print(f'Último nome: {nomeS [-1]}')