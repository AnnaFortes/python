from random import sample

jogadores = []

print('Valores sorteados: ')

for s in range (4):
    sorteio = sample(range(7), 1)
    jogador = f'Jogador {s+1}'
    jogadores.append({jogador : sorteio})
    
    print(f'\tO jogador {jogador} tirou {sorteio} ')
print()
print(jogadores)
print()

