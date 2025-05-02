from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['clt'] = int(input('Carteira de Trabalho (0 não tem): '))
ano_atual = date.today().year
idade2 = ano_atual - pessoa['idade']
pessoa['idade'] = idade2
if pessoa['clt'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    tempo_trabalhado = ano_atual - pessoa['contratação']
    aposentadoria = 35 - tempo_trabalhado
    idade_aposentar = idade2 + aposentadoria
    pessoa['aposentadoria'] = idade_aposentar
    if tempo_trabalhado >= 35:
        pessoa['aposentadoria'] = 'Aposentado(a)'
print('='*20)
for key, value in pessoa.items():
    print(f'- {key} tem o valor {value}')
print()