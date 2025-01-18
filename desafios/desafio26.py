nome = str(input('\nDigite seu nome completo: '))
nomeC = nome.split()
espaco = nome.replace(" ", "")
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(espaco)}')
print(f'Seu primeiro nome é {nomeC[0]} e ele tem {len(nomeC[0])} letras')

