numero = int(input('Numero: '))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(contador), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador-1
print(fatorial)
