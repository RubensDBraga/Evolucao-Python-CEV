from lib.interface import *


def arquivoexiste(nome):
    try:
        teste = open(nome, 'rt')
        teste.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        criar = open(nome, 'wt+')
        criar.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        ler = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        ler.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        cadas = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            cadas.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escritura dos dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            cadas.close()
