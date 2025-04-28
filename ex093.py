jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gol'] = gols
for n in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {n+1}? ')))
jogador['total'] = sum(gols)
print('='*20)
print(jogador)
print('='*20)
for key, value in jogador.items():
    print(f'O campo {key} tem valor {value}')
print('='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for posicao, lista in enumerate(gols):
    print(f' => Na partida {posicao+1}, fez {lista} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print()
