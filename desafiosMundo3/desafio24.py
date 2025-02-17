partidas = []

while True:
    jogadores = {}

    jogadores['nome'] = str(input('Nome do jogador: '))
    jogadores['jogos'] = int(input(f'Quantos jogos {jogadores['nome']} jogou? '))

    jogadores['gol'] = []
    jogadores['total'] = 0

    for j in range(jogadores['jogos']):
        gols = int(input(f'-> Quantos jogos na partida {j}? '))
        jogadores['gol'].append(gols)
        jogadores['total'] += gols
    
    partidas.append(jogadores)

    continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]

    print('-' * 40)

    if continuar == 'N':
        print('=-' * 30)
        break

print(partidas)
print(f'{"Cod":<3}{"nome":<15}{"gols":<20}{"total":<5}')

print('-' * 50)

for i, jogadores in enumerate(partidas):
    golFormatado = ', '.join(map(str, jogadores["gol"]))
    print(f'{i:<3}{jogadores["nome"]:<15}{golFormatado:<20}{jogadores["total"]:<5}')

print('-' * 50)

while True:
    print()
    dados = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    if dados == 999:
        print('-' * 40)
        print('<< VOLTE SEMPRE >>')
        print()
        break

    for i, jogadores in enumerate(partidas):
        if dados == i:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores['nome']}')
            for k, gols in enumerate(jogadores["gol"]):
                print(f'\tNo jogo(s) {k} fez {gols} gols.')


