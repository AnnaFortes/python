soma = 0
maior = 0
mult = 1

print('=-' * 20)
print('Escolha uma das opções abaixo: ')
print('=-'*20)
escolha = int(input('[1]Somar: \n[2]Multiplicar: \n[3]Maior de todos: \n[4]Novos números: \n[5]Sair: '))

for c in range(2):
    num = int(input('Digite um valor: '))
    soma += num
    mult *= num

    if num > maior:
        maior = num
while True:
    print('=-' * 20)
    print('Escolha uma das opções abaixo: ')
    print('=-'*20)
    escolha = int(input('[1]Somar: \n[2]Multiplicar: \n[3]Maior de todos: \n[4]Novos números: \n[5]Sair: '))
    if escolha == 1:
        print(f'A soma entre todos os números é {soma}')
    elif escolha == 2:
        print(f'A multiplicação entre todos os números é {mult}')
    elif escolha == 3:
        print(f'O maior número dentre todos é {maior}')
    elif escolha == 4:
        print('Digite novos números(digite 0 para voltar ao menu)')
        while True:
            num = int(input('Digite um valor: '))
            if num == 0:
                break
            soma += num
            mult *= num

            if num > maior:
                maior = num
    elif escolha == 5:
        print('FIM!')





