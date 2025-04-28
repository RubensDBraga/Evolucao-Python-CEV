import random
nome1 = input('Digite o primeiro concorrente: ')
nome2 = input('Digite o segundo concorrente: ')
nome3 = input('Digite o terceiro concorrente: ')
nome4 = input('Digite o quarto concorrente: ')
nome5 = input('Digite o quinto concorrente: ')
nomes = [nome1, nome2, nome3, nome4, nome5]
random.shuffle(nomes)
print('Ordem: ')
for i, nomes in enumerate(nomes, start=1):
    print(f'{i}.{nomes}')
