def aumentar(num=0):
    porcento = (num*10)/100
    valorat = num + porcento
    return valorat


def diminuir(num=0):
    porcento = (num*13)/100
    valorat = num - porcento
    return valorat


def dobro(num=0):
    drobo = num*2
    return drobo


def metade(num=0):
    met = num/2
    return met


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
