from datetime import date
atual = date.today().year
sex = int(input('1.Masculino\n2.Feminino\nQual seu sexo? '))
if sex == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sex == 2:
    print('Não é necessário o alistamento.')
else:
    print('Sexo não encontrado.')
