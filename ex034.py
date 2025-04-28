salario = float(input('\033[0;32;40mQual seu salário? \033[m'))
if salario > 1250:
    aumento = salario + (salario*10/100)
    print('\033[0;32;40mSeu novo salário é {:.2f}R$\033[m'.format(aumento))
else:
    aumento = salario + (salario*15/100)
    print('\033[0;32;40mSeu novo salário é {:.2f}R$\033[m'.format(aumento))
