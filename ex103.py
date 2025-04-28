def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)

'''
def detalhes(**info):
    print(f"Nome: {info.get('nome', 'Desconhecido')}")
    print(f"Idade: {info.get('idade', 'Não informada')}")

detalhes(nome="Ana")  
# Saída: 
# Nome: Ana
# Idade: Não informada
'''
