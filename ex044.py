print('-='*20)
print('{:-^38}'.format(' Compras '))
print('-='*20)
valor = float(input('Preço das compras: R$'))
print('''Forma de Pagamento.
1. à vista dinheiro/cheque
2. à vista cartão
3. 2x cartão
4. 3x ou mais cartão''')
forma = int(input('Qual a forma de pagamento? '))
if forma == 1:
    print('Terá 10% de desconto. Total a pagar: R${:.2f}'.format(
        valor-(valor/100*10)))
elif forma == 2:
    print('Terá 5% de desconto. Total a pagar: R${:.2f}'.format(
        valor-(valor/100*5)))
elif forma == 3:
    print('Total a pagar: R${:.2}'.format(valor))
elif forma == 4:
    vinte = valor + (valor * 20 / 100)
    qnt = int(input('Quantas parcelas? '))
    parcela = vinte / qnt
    print('''Sua compra será parcelada em {:.0f}x de R${:.2f} COM JUROS.
A compra de R${:.2f} vai custar R${:.2f} no final.'''.format(qnt, parcela, valor, vinte))
else:
    print('Forma de pagamento inválida.')
