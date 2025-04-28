def leiaint(num):
    while True:
        n = input(num)
        if n.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            print(f'Você acabou de digitar o número {n}')
            break


n = leiaint('Digite um número: ')
