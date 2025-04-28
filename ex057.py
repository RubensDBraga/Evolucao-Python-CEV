sexo = str(input('Qual seu sexo? Apenas [M/F]: ')).strip().upper()
while sexo not in 'MmFfMASCULINOFEMININO':
    sexo = str(input('ERRO, sexo não identificado. Qual seu sexo? Apenas [M/F]: ')).strip().upper()
print('Fim')
