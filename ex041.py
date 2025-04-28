from datetime import date
texto = 'Categorias'
largura = 38
print('=-'*20)
print(texto.center(largura))
print('=-'*20)
ano = int(input('Qual seu ano de nascimento? '))
anoat = date.today().year
idade = anoat - ano
if 1 <= idade <= 9:
    print('Você tem {} anos. Você se encaixa na categoria Mirim!'.format(idade))
elif 10 <= idade <= 14:
    print('Você tem {} anos. Você se encaixa na categoria Infantil!'.format(idade))
elif 15 <= idade <= 19:
    print('Você tem {} anos. Você se encaixa na categoria Junior!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos. Você se encaixa na categoria Sênior!'.format(idade))
else:
    print('Você tem {} anos. Você se encaixa na categoria MASTER!!'.format(idade))
