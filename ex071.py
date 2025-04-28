print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 100
contador_ced = 0
while True:
    if total >= ced:
        total -= ced
        contador_ced = contador_ced + 1
    else:
        if contador_ced > 0:
            print(f'Total de {contador_ced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contador_ced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!\n')
