c = ['\033[m',   #0 - sem cor
     '\033[34m', #1 - azul
     '\033[35m', #2 - roxo
     ]

def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

#programa principal
comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função da Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
print()

