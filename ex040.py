m1 = float(input('Primeira nota: '))
m2 = float(input('Segunda nota: '))
media = (m1+m2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(
    m1, m2, media))
if media < 5:
    print('Aluno reprovado')
elif media == 5 or media < 7:
    print('Aluno na recuperação')
else:
    print('Aluno aprovado')
