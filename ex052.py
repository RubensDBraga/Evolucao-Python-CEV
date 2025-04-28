numero = int(input('Digite the number: '))
total = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='- ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('O número é Primo')
else:
    print('O número não é Primo')
print('SayCat <3')
 