from lib.interface.funcoes import *
from lib.interface.arquivo.funcoes2 import *
from time import sleep

arq = 'desafioerro/minisistema/lib/interface/cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo exncontrado com sucesso!')
else:
    print('Arquivo não encontrado!')


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])

    if resposta== 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo \033[32m:)\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)

print()
