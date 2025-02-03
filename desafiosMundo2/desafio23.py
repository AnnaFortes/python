from random import randint
from time import sleep

print('=-' * 16)
print('\033[1;34m', ' ' * 7, 'JOGO DA ESCOLHA\033[m')
print('=-' * 16)

cont = 1
escolha = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
jog = int(input('Em que número eu pensei? [0 à 10] '))
sleep(0.5)

while escolha != jog: 
    cont += 1
    print('Que pena, você \033[31merrou :(\033[m')
    sleep(0.5)

    if jog < escolha:
        print('\033[33mMais...\033[m Tente mais uma vez!')
    elif jog > escolha:
        print('\033[33mMenos...\033[m Tente mais uma vez!')
    sleep(0.5)
    jog = int(input('Em que número eu pensei? [0 à 10] '))
    sleep(1)

if escolha == jog:
    sleep(1)
    print(f'\033[32mParabéns\033[m, você acertou! O número que pensei foi \033[33m{escolha}\033[m e ao total foram \033[33m{cont}\033[m tentativas!')
    
   
