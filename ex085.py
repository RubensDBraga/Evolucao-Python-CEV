lista = [[], []]
for n in range(7):
    valor = int(input(f'Digite o {n} número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os números pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')
