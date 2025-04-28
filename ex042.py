texto = 'Analisador de Triângulos'
largura = 38
print('=-'*20)
print(texto.center(largura))
print('=-'*20)
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t2 + t1:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if t1 == t2 == t3:
        print('Equilátero"')
    elif t1 != t2 != t3 != t1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar um triângulo.')
