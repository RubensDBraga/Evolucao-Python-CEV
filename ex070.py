total_compra = mil_reais = 0
print('-'*50)
print('LOJA SUPER BARATÃO'.center(50))
print('-'*50)
while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    nome_barato = nome_produto
    menor_preco = preco
    if preco > 1000:
        mil_reais = mil_reais + 1
    if preco < menor_preco:
        nome_barato = nome_produto
        menor_preco = preco
    total_compra = total_compra + preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA'.center(50, '-'))
print(f'O total da compra foi R${total_compra}')
print(f'Temos {mil_reais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${menor_preco}\n')
