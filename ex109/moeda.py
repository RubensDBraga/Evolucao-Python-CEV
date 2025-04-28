def aumentar(num=0, formata=False):
    porcento = (num*10)/100
    valorat = num + porcento
    return valorat if formata is False else moeda(valorat)


def diminuir(num=0, formata=False):
    porcento = (num*13)/100
    valorat = num - porcento
    return valorat if formata is False else moeda(valorat)


def dobro(num=0, formata=False):
    drobo = num*2
    return drobo if formata is False else moeda(drobo)


def metade(num=0, formata=False):
    met = num/2
    return met if formata is False else moeda(met)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
