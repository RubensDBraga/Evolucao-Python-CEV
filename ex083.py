expressao = str(input('Digite a expressão: '))
lista = []
for simb in expressao:
    if simb == '(':
        lista.append(simb)
    if simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(simb)
            break
if len(lista) > 0:
    print('Expressão inválida.')
else:
    print('Expressão de boa')
