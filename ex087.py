matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = tcoluna = maior_segl = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]: '))
print('-='*20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par = soma_par + matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos valores pares é {soma_par}')
for l in range(3):
    tcoluna = tcoluna + matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tcoluna}')
for c in range(3):
    if c == 0:
        maior_segl = matriz[1][c]
    if matriz[1][c] > maior_segl:
        maior_segl = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_segl}')
print()
