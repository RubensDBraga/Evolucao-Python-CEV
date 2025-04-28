lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print('-=-'*10)
print(f'Foram digitados {len(lista)} números')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'Ordem decrescente: {lista2}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição ', end='')
    for posicao, valores in enumerate(lista):
        if valores == 5:
            print(f'{posicao+1}... ', end='')
    print()
else:
    print('O valor 5 não foi digitado\n')
