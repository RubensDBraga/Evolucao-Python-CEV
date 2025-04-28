import random
import time
print('-='*20)
print(f'{'Palpites Mega-Sena':^40}')
print('-='*20)
sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'Sorteando {sorteio} jogos', '-='*3)
for jogo in range(sorteio):
    print(f'Jogo {jogo+1}: {[random.randint(1, 61) for _ in range(6)]}')
    time.sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)
print()
