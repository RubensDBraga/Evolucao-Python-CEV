def aumentar(num=0, aument=0, formata=False):
    porcento = (num*aument)/100
    valorat = num + porcento
    return valorat if formata is False else moeda(valorat)


def diminuir(num=0, dima=0, formata=False):
    porcento = (num*dima)/100
    valorat = num - porcento
    return valorat if formata is False else moeda(valorat)


def dobro(num=0, formata=False):
    drobo = num*2
    return drobo if formata is False else moeda(drobo)


def metade(num=0, formata=False):
    met = num/2
    return met if formata is False else moeda(met)


def resumo(val=0, aument=10, diminui=5):
    print('-'*34)
    print(f'{'RESUMO DO VALOR':^34}')
    print('-'*34)
    print(f'Preço analisado: \t{moeda(val)}')
    print(f'Metade do preço: \t{metade(val, True)}')
    print(f'Dobro do preço: \t{dobro(val, True)}')
    print(f'{aument}% de aumento: \t{aumentar(val, aument, True)}')
    print(f'{diminui}% de redução: \t{diminuir(val, diminui, True)}')
    print('-'*34)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
