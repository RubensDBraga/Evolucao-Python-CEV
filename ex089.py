alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-'*26)
print(f'{'No.':<4}{'Aluno':<10}{'Média':>8}')
print('-'*26)
for q, a in enumerate(alunos):
    print(f'{q:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*26)
while True:
    aluno_notas = int(input('Mostrar notas de qual aluno? (999 para sair)'))
    if aluno_notas == 999:
        print()
        print('Finalizando...')
        break
    if aluno_notas <= len(alunos)-1:
        print(
            f'Notas de {alunos[aluno_notas][0]} são {alunos[aluno_notas][1]}')
    else:
        print('Tente novamente')
print()
print('<<< Volte Sempre >>>')
