num = int(input('\nDigite um número: '))
print('Escolha a opção para a conversão:')
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
escolha = int(input('Digite a opção escolhida: '))
if escolha == 1:
    binario = bin(num)[2:]
    print(f'BINÁRIO: {binario}')
elif escolha == 2:
    octal = oct(num)[2:]
    print(f'OCTAL: {octal}')
elif escolha == 3:
    hexa = hex(num)[2:]
    print(f'HEXADECIMAL: {hexa}')
else:
    print('Opção inválida! Por favor, digite uma opção válida!')
