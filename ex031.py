viaj = float(input('Qual a distância da viagem? '))
if viaj <= 200:
    v1 = viaj*0.50
    print('Sua viagem custará R${}'.format(v1))
else:
    v2 = viaj*0.45
    print('Sua viagem custará R${}'.format(v2))
