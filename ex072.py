import num2words
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20)
cont = 'S'
while cont == 'S':
    while True:
        numer = int(input('Digite um número entre 0 e 20: '))
        if numer < 0 or numer > 20:
            print('Tente novamente.', end=' ')
        else:
            break
    print(
        f'Você digitou o número {num2words.num2words(numeros[numer], lang='pt_BR')}\n')
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(
            input('Informação inválida. Deseja continuar? [S/N] ')).strip().upper()
