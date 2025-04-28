cadastro = dict()
cadastro_lista = list()
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    cadastro['idade'] = int(input('Idade: '))
    soma = soma + cadastro['idade']
    cadastro_lista.append(cadastro.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('='*20)
print()
print(f'A) Ao todo temos {len(cadastro_lista)} pessoas cadastradas.')
media = soma / len(cadastro_lista)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in cadastro_lista:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa['nome']}', end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for pessoa in cadastro_lista:
    if pessoa['idade'] > media:
        print(' ')
        for key, value in pessoa.items():
            print(f'{key} = {value}', end='; ')
print()
print('\nCABOOO')
