texto = 'Calculadora de IMC'
largura = 38
print('-='*20)
print(texto.center(largura))
print('-='*20)
peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (M) '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Você está abaixo do peso. Seu IMC é de {:.1f}.'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no peso ideal. Seu IMC é de {:.1f}.'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso. Seu IMC é de {:.1f}.'.format(imc))
elif 30 <= imc < 40:
    print('Você está com grau de obesidade. Seu IMC é de {:.1f}'.format(imc))
elif imc > 40:
    print('Você está com obsidade morbida. Seu IMC é de {:.1f}.'.format(imc))
