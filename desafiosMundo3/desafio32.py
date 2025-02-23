jogador = {}

def ficha(nome=False, gol=False):

    print('-' * 35)
    
    nome = str(input('Nome do jogador: '))

    gols = input('Quantidade de gols: ')

    if not nome:
        nome = '<desconhecido>'

    if not gols:
        gols = 0
    else:
        gols = int(gols)

    jogador['nome'] = nome
    jogador['gols'] = gols

    return jogador


resul = ficha(nome=True, gols=True)

print(f'O jogador {jogador["nome"]} fez {jogador["gols"]} gol(s) no campeonato.')
print()
