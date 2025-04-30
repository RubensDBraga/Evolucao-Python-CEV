import random
numeros = [random.randint(1, 100) for _ in range(5)]
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}\n')