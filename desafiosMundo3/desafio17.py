from random import randint
from time import sleep

print('-' * 50)
print('JOGO DA MEGA SENA'.center(50))
print('-' * 50)

jogadas = int(input('Quantos jogos você que que eu sorteie? '))

tdsJogos = [] 

for j in range(jogadas):
    jogo = []

    while len(jogo) < 6: 
        num = randint(1, 60)
        if num not in jogo: 
            jogo.append(num) 
    tdsJogos.append(sorted(jogo)) 

sleep(0.5)
print(f'=-=-=-=-= SORTEANDO {jogadas} JOGOS =-=-=-=-=')
sleep(1)

for i, jogo in enumerate(tdsJogos, 1): 
    print(f'Jogo {i}: {sorted(jogo)}')
    sleep(1)

print('=-=-=-=-=- < BOA SORTE! > =-=-=-=-=-')
print()