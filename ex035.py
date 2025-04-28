print('\033[34m-=\033[m'*20)
print('\033[0;36;40mAnalisador de Triângulos\033[m')
print('\033[33m-=\033[m'*20)
r1 = float(input('\033[0;36;40mPrimeiro segmento: \033[m'))
r2 = float(input('\033[0;36;40mSegundo segmento: \033[m'))
r3 = float(input('\033[0;36;40mTerceiro segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  
    print('\033[0;36;40mOs segmentos acima podem formar triângulo.\033[m')
else:
    print('\033[0;31;40mOs segmentos acima não podem formar triângulo.\033[m')
