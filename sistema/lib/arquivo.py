from lib.interface import *

def arqExiste(nome):
    import os
    os.chdir(r"c:/Users/Notebook/Documents/phyton/python/sistema")
    
    try:
        abrir = open(nome, 'rt')
        abrir.close()
        return True

    except FileNotFoundError:
        return False

def criarArquivo(nome):
    try:
        abrir = open(nome, 'wt+')
        abrir.close()
    
    except:
        print('Ouve um ERRO na criação do arquivo!')

    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        abrir = open(nome, 'rt')

    except:
        print('Erro ao ler o arquivo!')

    else:
        cabeçalho('PESSOAS CADASTRADAS')

        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        abrir.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        abrir = open(arq, 'at')
    
    except:
        print('Ouve um ERRO na abertura do arquivo')

    else:
        try:
            abrir.write(f'{nome}; {idade}\n')

        except:
            print('Ouve um ERRO na hora de escrever os dados!')

        else:
            print(f'Novo registro de {nome} adicionado')
            abrir.close()
