situa = dict()
situa['nome'] = str(input('Nome: '))
situa['média'] = float(input(f'Média de {situa['nome']}: '))
if situa['média'] < 6:
    situa['situação'] = 'Reprovado'
if 5 <= situa['média'] < 6:
    situa['situação'] = 'Recuperação'
else:
    situa['situação'] = 'Aprovado'
for key, value in situa.items():
    print(f'- {key} é igual a {value}')
