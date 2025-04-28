from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('Jogador Ganhou!')
        elif jogador == 2:
            print('Computador Ganhou!')
    elif computador == 1:
        if jogador == 0:
            print('Computador Ganhou!')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('Jogador Ganhou!')
    elif computador == 2:
        if jogador == 0:
            print('Jogador Ganhou!')
        elif jogador == 1:
            print('Computador Ganhou!')
        elif jogador == 2:
            print('EMPATE')
else:
    print('Jogada inválida')
# from random import choice
# from time import sleep
# pedra = 'Pedra'
# papel = 'Papel'
# tesoura = 'Tesoura'
# lista = [pedra, papel, tesoura]
# aleat = choice(lista)
# print('-='*20)
# print('''Vamos jogar Jokenpô!!
# Tente me ganhar!''')
# print('-='*20)
# escolha = (input('Qual sua escolha? Pedra, Papel ou Tesoura? ')).strip().upper()
# teste = escolha.isnumeric()
# teste2 = 'PEDRA' in escolha
# teste3 = 'PAPEL' in escolha
# teste4 = 'TESOURA' in escolha
# if teste == True:
#    print('Não é assim que se joga.')
# elif teste2 == False and teste3 == False and teste4 == False:
#    print('Não é assim que se joga.')
# else:
#    print('JO')
#    sleep(1)
#    print('KEN')
#    sleep(1)
#    print('PÔ')
#    print('Eu joguei {}!'.format(aleat))
#    if escolha == 'PEDRA' and aleat == pedra or escolha == 'PAPEL' and aleat == papel or escolha == 'TESOURA' and aleat == tesoura:
#        print('Empatamos')
#    elif escolha == 'PEDRA' and aleat == papel:
#        print('Ganhei!')
#    elif escolha == 'PEDRA' and aleat == tesoura:
#        print('Droga, você ganhou.')
#    elif escolha == 'PAPEL' and aleat == tesoura:
#        print('Ganhei!')
#    elif escolha == 'PAPEL' and aleat == pedra:
#        print('Droga, você ganhou.')
#    elif escolha == 'TESOURA' and aleat == pedra:
#        print('Ganhei!')
#    elif escolha == 'TESOURA' and aleat == papel:
#        print('Droga, você ganhou.')
