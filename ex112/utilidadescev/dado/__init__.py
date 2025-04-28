def validador(msg):
    validar = False
    while validar is False:
        pergunt = str(input(msg)).strip().replace(',', '.')
        if pergunt.isalpha() or pergunt == '':
            print(f'\033[31mERRO: {pergunt} é um preço inválido!\033[m')
        else:
            validar = True
            return float(pergunt)
