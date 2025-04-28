import moeda
val = float(input('Valor: '))
print(f'A metade de {moeda.moeda(val)} é {moeda.metade(val, True)}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.dobro(val, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(val, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(val, True)}')
