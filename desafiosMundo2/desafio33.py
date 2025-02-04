from random import randint
from time import sleep

soma = cont = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:
    num = int(input('Digite um valor: '))
    jog = str(input('PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    print('-' * 25)

    comp = randint(1, 100)
    soma = num + comp

    res = 'PAR' if soma % 2 == 0 else 'IMPAR'

    sleep(1)
    print(f'Você jogou {num} e o computador jogou {comp}. Total de {soma} DEU {res}')
    print('-' * 25)

    if res[0] == jog:
        print('Você VENCEU! \nVamos jogar novamente... ')
        print('-' * 25)
        cont += 1
        sleep(1)
    else:
        print(f'Você PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break

    
    
