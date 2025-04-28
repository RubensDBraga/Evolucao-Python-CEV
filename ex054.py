import datetime
anoat = datetime.date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    idade = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    if anoat - idade >= 18:
        cont = cont+1
    else:
        cont2 = cont2+1
print('\nAo todo tivemos {} pessoa maiores de idade.'.format(cont))
print('E também tivemos {} pessoas menores de idade.\n'.format(cont2))
