lista1 = []
while True:
    lista1.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
lista_par = []
lista_impar = []
for valor in lista1:
    if valor % 2 == 0:
        lista_par.append(valor)
    if valor % 2 != 0:
        lista_impar.append(valor)
print('-=-'*10)
print(f'Primeira lista: {lista1}')
print(f'Números pares: {lista_par}')
print(f'Números ímpares: {lista_impar}')
