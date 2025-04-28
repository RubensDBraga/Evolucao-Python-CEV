nome_peso = []
auxiliar = []
pesado = leve = 0
while True:
    auxiliar.append(str(input('Digite o nome: ')))
    auxiliar.append(float(input('Digite o peso: ')))
    if len(nome_peso) == 0:
        pesado = leve = auxiliar[1]
    else:
        if pesado < auxiliar[1]:
            pesado = auxiliar[1]
        if leve > auxiliar[1]:
            leve = auxiliar[1]
    nome_peso.append(auxiliar[:])
    auxiliar.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print('=-='*10)
print(f'Foram cadastradas {len(nome_peso)} pessoas.')
print(f'O maior peso foi de {pesado}. Peso de ', end='')
for p in nome_peso:
    if p[1] == pesado:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leve}. Peso de ', end='')
for p in nome_peso:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print()
