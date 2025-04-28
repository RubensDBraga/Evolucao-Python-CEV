import math
n = float(input('Digite um ângulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print(
    'Seno é: {:.2f} \nO Cosseno é: {:.2f} \nE a Tangente é: {:.2f}'.format(s, c, t))
