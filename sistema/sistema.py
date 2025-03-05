from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])

    if resposta == 1:
        #listar conteudo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        #cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo \033[32m:)\033[m')
        break

    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)

print()
