from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('\nValores sorteados:')
print()
for key, value in jogo.items():
    print(f'{key} tirou {value} no dado')
    sleep(0.5)
print('='*30)
print('\n== RANKING DOS JOGADORES ==')
print()
jogo_organizado = ()
jogo_organizado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for number, lista in enumerate(jogo_organizado):
    print(f'{number+1} lugar: {lista[0]} com {lista[1]}')
    sleep(0.5)
print()
