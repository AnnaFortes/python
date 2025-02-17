#aprimore o desafio do jogador de futebol para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
jogadores = {}

while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogadores['jogos'] = int(input(f'Quantos jogos {jogadores['nome']} jogou? '))

    for j in range(jogadores['jogos']):
        jogadores['qntJogos'] = int(input(f'-> Quantos jogos na partida {j}? '))
    

    continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()[0]

    print('-' * 40)

    if continuar == 'N':
        print('=-' * 30)
        break

print(f'{"cod nome":<15}{"gols":<10}{"total":<5}')
print('-' * 40)


