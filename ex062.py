print('Gerador de PA')
print('=-='*10)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(numero), end='')
        numero = numero + razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
