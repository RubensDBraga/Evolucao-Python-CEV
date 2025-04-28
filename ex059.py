import time
valor1 = float(input('Primeiro número: '))
valor2 = float(input('Segundo valor: '))
escolha = 0
print('=-='*10)
while escolha != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair\n''')
    escolha = int(input('Qual opção deseja: '))
    if escolha == 1:
        soma = valor1 + valor2
        print('\nOpção de Soma escolhida.')
        print('A soma dos valores é: {}'.format(soma))
    if escolha == 2:
        mult = valor1 * valor2
        print('\nOpção de multiplicação escolhida.')
        print('A multiplicação dos valores é: {}'.format(mult))
    if escolha == 3:
        maior = valor1
        if valor1 < valor2:
            maior = valor2
        print('\nOpção ''maior'' escolhida.')
        print('O maior número dos valores digitados é: {:.2f}'.format(maior))
    if escolha == 4:
        valor1 = float(input('Primeiro número: '))
        valor2 = float(input('Segundo valor: '))
    if escolha >= 6:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
    time.sleep(1)
print('Fim do programa. Volte sempre!')
