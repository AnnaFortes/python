from random import sample
from time import sleep
from operator import itemgetter

jogadores = []
ranking = {}

print('Valores sorteados: ')

for s in range(4):
    sorteio = sample(range(7), 1)[0]
    jogador = {"nome": f"Jogador {s+1}", "valor": sorteio}
    jogadores.append(jogador)
    
    print(f'\tO {jogador["nome"]} tirou {jogador["valor"]} no dado. ')
    sleep(1)

print()
print(jogadores)

ranking = sorted(jogadores,  key=itemgetter("valor"), reverse=True)

print('\nRanking dos jogadores: ')
for pos, jogador in enumerate(ranking, 1): 
    print(f'\t{pos}° lugar: {jogador["nome"]} com {jogador["valor"]}.')
    sleep(1)
print()

