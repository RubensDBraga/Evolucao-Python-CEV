from time import sleep


def maior(*valor):
    # Posso botar ''bigger = max(valor)'' Mas eu teria que mudar os IF para verificar se existe número dentro da função ou não
    bigger = 0
    for num in valor:
        if num > bigger:
            bigger = num
    print('='*40)
    print('Analisando os valores processados...')
    print()
    for num in valor:
        print(f'{num}', end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {bigger}.')
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print()
