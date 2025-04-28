def voto(idade):
    import datetime
    an = datetime.date.today().year
    idad = an - idade
    if 65 > idad >= 18:
        return f'Com {idad} anos: VOTO OBRIGATÓRIO'
    if idad < 18:
        return f'Com {idad} anos: NÃO VOTA'
    if idad >= 65:
        return f'Com {idad} anos: VOTO OPCIONAL'


ano = int(input('Em que ano nasceu: '))
print(voto(ano))
