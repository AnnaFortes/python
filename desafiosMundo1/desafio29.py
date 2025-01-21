num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é \033[34m PAR\033[m ')
else:
    print(f'O número {num} é \033[31m ÍMPAR\033[m ')