#escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido, o programa devera escrever na tela se o usuario venceu ou nao
from random import randint
num = randint(1, 5)
escolha = int(input('Escolha um número entre 1 e 5: '))
if num == escolha:
    print('Parabéns, você acertou! ')
else:
    print('Tente outra vez!')