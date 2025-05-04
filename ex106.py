def infos(func):
    while True:
        entrada = str(input(func)).strip().lower()
        if entrada == 'fim':
            texto = 'Até logo!'
            tiu = len(texto) + 4
            print('~'*tiu)
            print(f'  {texto}  ')
            print('~'*tiu)
            break
        texto = f"Acessando o manual do comando '{entrada}'"
        tiu = len(texto) + 4
        print('~'*tiu)
        print(f'  {texto}  ')
        print('~'*tiu)
        help(entrada)


infos('Função ou Biblioteca > ')
