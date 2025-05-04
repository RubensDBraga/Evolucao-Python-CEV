def notas(*noti, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param noti: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    media = sum(noti)/len(noti)
    situ = ''
    if media >= 7:
        situ = 'BOA'
    if media >= 5:
        situ = 'RAZOÁVEL'
    else:
        situ = 'RUIM'
    diquit = {'total': len(noti), 'maior': max(noti), 'menor': min(
        noti), 'media': media, 'situacao': situ}
    if sit == False:
        del diquit['situacao']
    return diquit


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print()
help(notas)
