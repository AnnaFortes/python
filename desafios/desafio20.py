#crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas, todas as minusculas, quantas letras ao todo sem considerar espaços e quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
nomec = nome.split()
print(len(''.join(nomec)))
nome1 = nome.split()
print(len(nome1[0]))