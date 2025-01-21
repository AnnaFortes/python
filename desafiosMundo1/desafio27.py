from random import randint
from time import sleep
#estudar sobre a biblioteca time
num = randint(0, 5)
print('-=-' * 20)
print('\nVou pensar em um número entre 0 e 5, tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #tempo de espera de 2 segundos
if num == jogador:
    print('PARABÉNS, você conseguiu me vencer! ')
else:
    print(f'GANHEI! Eu pensei no número {num} e não no {jogador}!')