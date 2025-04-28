jogador = dict()
gols = list()
jogador_lista = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for n in range(partidas):
        gols.append(int(input(f'    Quantos gols na partida {n+1}? ')))
    jogador['gol'] = gols[:]
    jogador['total'] = sum(gols)
    jogador_lista.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        print('Digite algo válido')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('='*20)
print()
print('Cod ', end='')
for key in jogador.keys():
    print(f'{key:<14} ', end='')
print()
print('-'*40)
for key, joga in enumerate(jogador_lista):
    print(f'{key:>3} ', end='')
    for values in joga.values():
        print(f'{str(values):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Estatísticas do jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogador_lista):
        print('Jogador inválido')
    else:
        print(
            f'-- LEVANTAMENTO DO JOGADOR {jogador_lista[busca]['nome']} --'.upper())
        for kay, val in enumerate(jogador_lista[busca]['gol']):
            print(f'    No jogo {kay+1} fez {val} gols.')
