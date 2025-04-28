frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[l]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Palíndromo')
else:
    print('Não palíndromo')
