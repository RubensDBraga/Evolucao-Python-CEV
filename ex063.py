quantidade = int(input('Quantos termos: '))
repeticao = 3
n1 = 0
n2 = 1
if quantidade == 1:
    print('0')
else:
    print('{} -> {} -> '.format(n1, n2), end='')
    while repeticao <= quantidade:
        n3 = n1 + n2
        print('{} -> '.format(n3), end='')
        n1 = n2
        n2 = n3
        repeticao += 1
print('Fim.')
