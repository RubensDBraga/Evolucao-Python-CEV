import moeda
val = float(input('Valor: '))
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(val))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(val))}')
