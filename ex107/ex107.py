import moeda
val = float(input('Valor: '))
print(f'A metade de {val} é {moeda.metade(val)}')
print(f'O dobro de {val} é {moeda.dobro(val)}')
print(f'Aumentando 10% temos {moeda.aumentar(val)}')
print(f'Reduzindo 13% temos {moeda.diminuir(val)}')
