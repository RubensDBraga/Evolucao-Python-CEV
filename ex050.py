soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Número {}: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} número PARES; A soma dos números PARES é: {}'.format(cont, soma))
