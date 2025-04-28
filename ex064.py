numero = float(input('Digite o número [999 para parar]: '))
acumulador = 0
digitados = 0
while numero != 999:
    acumulador += numero
    digitados += 1
    numero = float(input('Digite o número [999 para parar]: '))
print('A some entre os {} números digitados da: {}'.format(digitados, acumulador))
