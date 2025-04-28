pessoa18 = homem = mulher = mulher20 = 0
while True:
    print('-'*22)
    print('Cadastre uma pessoa')
    print('-'*22)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F':
        mulher = mulher + 1
    if idade > 18:
        pessoa18 = pessoa18 + 1
    if idade < 20 and sexo == 'F':
        mulher20 = mulher20 + 1
    print('-'*22)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break
print('====== FIM DO PROGRAMA ======\n')
print(f'Total de pessoas com mais de 18 anos: {pessoa18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Ao todo temos {mulher} mulheres cadastradas')
print(f'E temos {mulher20} mulheres com menos de 20 anos\n')
