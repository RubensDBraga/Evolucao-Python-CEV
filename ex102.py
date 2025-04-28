def fatorial(num, show=False):
    """
    --> Calcula o Fatorial de um número.
    param num: O número a ser calculado.
    param show: (OPCIONAL) Mostrar ou não a conta.
    return: O valor do Fatorial de um número n
    """
    fat = 1
    for f in range(num, 0, -1):
        fat = fat * f
        if show == True:
            print(f, end='')
            if f > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fat


print(fatorial(5, True))
print()
help(fatorial)
