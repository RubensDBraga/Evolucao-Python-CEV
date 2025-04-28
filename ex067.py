while True:
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    if tabu <= 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-'*20)
    contador = 1
    while contador <= 10:
        mult = tabu * contador
        print(f'{tabu} x {contador} = {mult}')
        contador = contador + 1
    print('-'*20)
