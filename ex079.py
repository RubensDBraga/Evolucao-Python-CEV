lista = []
while True:
    valores = int(input('Digite um valor: '))
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print()
lista.sort()
print(lista)
