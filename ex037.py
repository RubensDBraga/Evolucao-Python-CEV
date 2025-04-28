n = int(input('Digite um número inteiro qualquer: '))
print('=-'*20)
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('=-'*20)
forma = int(input('Qual conversão deseja? '))
if forma == 1:
    print('A conversão do número {} para Binário é: {}.'.format(
        n, bin(n).lstrip('0b')))
elif forma == 2:
    print('A conversão do número {} para Octal é: {}'.format(n, oct(n).lstrip('0o')))
elif forma == 3:
    print('A conversão do número {} para Hexadecimal é: {}'.format(
        n, hex(n)[2:]))
else:
    print('Conversão não encontrada')
