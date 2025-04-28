import random
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n = random.randint(0, 5)
u = int(input('Em que número pensei? '))
print('Processando...')
sleep(1)
if u == n:
    print('Acertou! O número foi {}'.format(n))
else:
    print('Não foi dessa vez. O número foi {}'.format(n))
