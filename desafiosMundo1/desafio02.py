algo = input('Digite algo: ')
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m'
}
print(f'Tipo: {cores['amarelo']}{type(algo)}{cores['limpa']}')
print(f'Tem número: {cores['azul']}{algo.isnumeric()}{cores['limpa']} ')
print(f'Tem letra: {cores['ciano']}{algo.isalpha()}{cores['limpa']}')
print(f'É alfanúmerico: \033[4m{cores['cinza']}{algo.isalnum()}{cores['limpa']}')
print(f'Tem espaço: {cores['magenta']}{algo.isspace()}{cores['limpa']}')
print(f'Tem letras maiusculas: {cores['verde']}{algo.isupper()}{cores['limpa']}')
print(f'Tem letra minuscula: \033[1m{algo.islower()}{cores['limpa']}')
print(f'Está capitalizada: {cores['vermelho']}{algo.istitle()}{cores['limpa']}')

