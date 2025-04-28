from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['clt'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['clt'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    ano_atual = date.today().year
    tempo_trabalhado = ano_atual - pessoa['contratação']
    aposentadoria2 = 35 - tempo_trabalhado
    idade2 = ano_atual - pessoa['idade']
    idade_aposentar = idade2 + aposentadoria2
    pessoa['idade'] = idade2
    pessoa['aposentadoria'] = idade_aposentar
    if tempo_trabalhado >= 35:
        pessoa['aposentadoria'] = 'Aposentado(a)'
print('='*20)
for key, value in pessoa.items():
    print(f'- {key} tem o valor {value}')
print()
