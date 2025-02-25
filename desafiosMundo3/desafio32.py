def ficha(nome='<desconhecido>', gol=0):
    """ 
    Exibe a ficha de um jogador, incluindo nome e quantidade de gols.

    :param nome: Nome do jogador. Se não informado, será <desconhecido>.
    :param gol: Quantidade de gols. Se não informado, será 0.
    :return: Dicionário com os dados do jogador.
    """
    
    print('-' * 35)

    # Se não for passado um nome, mantém o padrão '<desconhecido>'
    nomeInput = input('Nome do jogador: ').strip()
    if nomeInput:  # Se o usuário digitar algo, substitui o nome
        nome = nomeInput  

    # Se não for passado um número de gols, mantém 0
    golsInput = input('Quantidade de gols: ').strip()
    if golsInput.isdigit():  # Verifica se foi digitado um número
        gol = int(golsInput)

    jogador = {'nome': nome, 'gols': gol}  

    return jogador


resul = ficha()

print(f'O jogador {resul["nome"]} fez {resul["gols"]} gol(s) no campeonato.')
print()
