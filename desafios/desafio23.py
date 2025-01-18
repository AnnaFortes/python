#leia o nome de uma pessoa e diga se ela tem silva no nome
nome = str(input('Digite seu nome: ')).strip().lower()
print(f'Seu nome tem Silva? {'silva' in nome}')