from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo == 1
    if inicio > fim:
        passo = -abs(passo)
        for cont in range(inicio, fim-1, passo):
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
    else:
        passo = abs(passo)
        for cont in range(inicio, fim+1, passo):
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
