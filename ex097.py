def escreva(msg):
    tamanho = len(msg)+4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)


escreva(str(input('Frase: ')))
