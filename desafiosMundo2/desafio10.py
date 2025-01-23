import emoji
from random import choice
from time import sleep
print('Escolha com oque jogar: ')
print(emoji.emojize('1 - Para pedra :moyai:', language='alias'))
print(emoji.emojize('2 - Para papel :memo:', language='alias'))
print(emoji.emojize('3 - Tesoura :scissors:', language='alias'))
escolha = int(input('Digite a opção escolhida: '))

escolha2 = choice([1, 2, 3])
sleep(1)

if escolha2 == 1:
    print(f'Jogador 2 escolheu:  {emoji.emojize(':moyai:', language='alias')}')
elif escolha2 == 2: 
    print(f'Jogador 2 escolheu:  {emoji.emojize(':memo:', language='alias')}')
else:
    print(f"Jogador 2 escolheu: {emoji.emojize(':scissors:', language='alias')}")

sleep(2)

if escolha == escolha2:
    print('Empate!')
elif (escolha == 1 and escolha2 == 3) or (escolha == 2 and escolha2 == 1) or (escolha == 3 and escolha2 == 2):
    print('Jogador 1 venceu!')
else: 
    print('Jogagor 2 venceu!')
    