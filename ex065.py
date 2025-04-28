continua = 'S'
contador = 0
acumulador = 0
maior = 0
menor = 0
while continua in 'Ss':
    numeros = int(input('Números: '))
    acumulador += numeros
    if contador == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    continua = str(input('Continua [S/N]? ')).strip()
    contador += 1
media = acumulador/contador
print('Você digitou {} números e a média foi {:.2f}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
