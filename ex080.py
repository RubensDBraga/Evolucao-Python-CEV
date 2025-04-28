lista = []
for l in range(5):
    valores = int(input('Digite o valor: '))
    if l == 0 or valores > lista[-1]:
        lista.append(valores)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos = pos + 1
print()
print(lista)
