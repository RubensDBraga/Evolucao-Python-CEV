def area(a, b):
    result = a * b
    print(f'A área de um terreno {a}x{b} é de {result}m2')


print('Controle de terrenos')
print('-'*20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
