jogo = {}

jogo['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))

jogo['gol'] = []
jogo['total'] = 0

for j in range(partidas):
    gols = int(input(f'\tQuantos gols na partida {j}? '))

    jogo['gol'].append(gols)

    jogo['total'] += gols

print('=-' * 30)
print(jogo)
print('=-' * 30)
 
for chave, valor in jogo.items():
    print(f'O campo {chave} tem o valor {valor}')
print('=-' * 30)

print(f'O jogador {jogo["nome"]} jogou {partidas} partidas.')

for p, k in enumerate(jogo['gol']):
    print(f'\t=> Na partida {p}, fez {k} gols')

print()

