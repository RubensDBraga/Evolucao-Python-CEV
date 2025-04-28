import random
numerorandom = random.randint(0, 10)
acumulador = 0
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
escolha = int(input('\nQual número pensei? '))
while escolha != numerorandom:
    acumulador = acumulador+1
    if escolha > numerorandom:
        print('Menos...', end=' ')
    if escolha < numerorandom:
        print('Mais...', end=' ')
    escolha = int(input('Escolha um número: '))
print('Conseguiu!! O número foi {}. Você precisou de {} tentativas.\n'.format(
    numerorandom, acumulador))

'''import random
numerorandom = random.randint(0, 10)
acumulador = 0
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
escolha = int(input('\nQual número pensei? '))
while escolha != numerorandom:
    acumulador = acumulador+1
    print('Você errou, o número era {}. Vamos novamente!'.format(numerorandom))
    numerorandom = random.randint(0, 10)
    escolha = int(input('\nEscolha um número entre 0 e 10: '))
print('Conseguiu!! O número foi {}. Você precisou de {} tentativas.\n'.format(
    numerorandom, acumulador))'''
