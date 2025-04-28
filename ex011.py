n = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))
a = n*n2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(n, n2, a))
t = a/2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))
