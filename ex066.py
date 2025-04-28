soma = 0
contador = 0
while True:
    numeros = int(input('Digite um número [999 para parar]: '))
    if numeros == 999:
        break
    soma = soma + numeros
    contador = contador + 1
print(f'A soma dos {contador} valores foi {soma}!')
