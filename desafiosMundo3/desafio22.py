jogo = {}

jogo['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))

jogo['gol'] = []
jogo['total'] = 0

for j in range(partidas):
    gols = int(input(f'Quantos gols na partida {j}? '))

    jogo['gol'].append(gols)

    jogo['total'] += gols

print('=-' * 30)
print(jogo)
print('=-' * 30)
print(f'O campo nome tem o valor {jogo["nome"]}.')
print(f'O campo gols tem o valor {jogo["gol"]}.')
print(f'O campo total tem o valor {jogo["total"]}.')
print('=-' * 30)

print(f'O jogador {jogo["nome"]} jogou {partidas} partidas.')

for p, k in enumerate(jogo['gol']):
    print(f'\t=> Na partida {p}, fez {k} gols')

print()

