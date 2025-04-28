termo = int(input('Primeiro termo: '))
rpa = int(input('PA: '))
dez = termo + (10-1) * rpa
for c in range(termo, dez + rpa, rpa):
    print(c)
