import random
vitorias = 0
while True:
    print('=-='*10)
    print('Par ou Ímpar!'.center(30))
    print('=-='*10)
    escolha = str(input('\nQual você quer ser [P/I]? ')).strip().upper()
    if escolha in 'I':
        aleatorio = random.randint(0, 10)
        print('\nÓtimo, eu serei Par!')
        numero = int(input('Vamos jogar [Digite um número]: '))
        print('-'*55)
        resultado = (aleatorio+numero) % 2
        if resultado == 0:
            print(
                f'Ganhei!! Eu escolhi {aleatorio} e você {numero}. Total de {aleatorio+numero}. DEU PAR')
            print('-'*55)
            print('Você PERDEU!')
            break
        else:
            print(
                f'Perdi. Eu escolhi {aleatorio} e você {numero}. Total de {aleatorio+numero}. DEU ÍMPAR\n')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias = vitorias + 1
    if escolha in 'P':
        aleatorio = random.randint(0, 10)
        print('\nÓtimo, eu serei Ímpar!')
        numero = int(input('Vamos jogar [Digite um número]: '))
        print('-'*55)
        resultado = (aleatorio+numero) % 2
        if resultado != 0:
            print(
                f'Ganhei!! Eu escolhi {aleatorio} e você {numero}. Total de {aleatorio+numero}. DEU ÍMPAR')
            print('-'*55)
            print('Você PERDEU!')
            break
        else:
            print(
                f'Perdi. Eu escolhi {aleatorio} e você {numero}. Total de {aleatorio+numero}. DEU PAR\n')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias = vitorias + 1
print('=-='*18)
print(f'GAME OVER! Você terminou com {vitorias} vitórias.\n')
