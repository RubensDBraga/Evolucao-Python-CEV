print('Gerador de PA')
print('=-='*10)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = numero
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    contador += 1
print('Fim')
