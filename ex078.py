valores = [int(input('Digite um número: ')) for _ in range(5)]
maior = max(valores)
menor = min(valores)
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao+1}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao+1}... ', end='')
print()
