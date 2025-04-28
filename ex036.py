texto = 'Consultoria de Empréstimos'
largura = 38
print('=-'*20)
print(texto.center(largura))
print('=-'*20)
cas = float(input('Qual valor da casa? '))
sal = float(input('Qual seu salário? '))
tep = float(input('Em quantos anos pretende pagar? '))
meses = tep*12
prestmen = cas/meses
trintasal = sal*30/100
if prestmen > trintasal:
    print('O empréstimo foi negado')
else:
    print('Você terá que pagar R${:.2f} por mês.'.format(prestmen))
    print('Empréstimo aprovado!')
