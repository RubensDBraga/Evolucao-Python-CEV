from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(5):
        num = randint(1, 10)
        print(f'{num}', end=' ', flush=True)
        lista.append(num)
        sleep(0.5)
    print('Sorteados!')


def somapar(somar):
    somada = 0
    for nu in numeros:
        if nu % 2 == 0:
            somada = somada + nu
    print(f'Somando os valores pares de {numeros}, temos: {somada}')


sorteia(numeros)
somapar(numeros)
