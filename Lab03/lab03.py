###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# leitura de dados

ds = int(input())
hs = int(input())
ms = int(input())
est = str(input())
mp = str(input())

# valor dos ingressos 

pv_1_7 = 30
pv_2_3_4 = 15
pv_5_6 = 20

pn_1_4_5 = 30
pn_2_3 = 20
pn_6_7 = 40

# valor a pagar


if est == "S":
    if hs == 18:
        if ms >= 30:
            if ds == 1 or ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.5, '.2f').replace('.', ','))
            elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3*0.5, '.2f').replace('.', ','))
            elif ds == 6 or ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7*0.5, '.2f').replace('.', ','))   
        else:
            if ds == 1 or ds == 7:
                    print('Valor do ingresso: R$', format(pv_1_7*0.5, '.2f').replace('.', ','))
            elif ds == 2 or ds == 3 or ds == 4:
                    print('Valor do ingresso: R$', format(pv_2_3_4*0.5, '.2f').replace('.', ','))
            elif ds == 5 or ds == 6:
                    print('Valor do ingresso: R$', format(pv_5_6*0.5, '.2f').replace('.', ','))
    elif hs < 18:
        if ds == 1 or ds == 7:
                    print('Valor do ingresso: R$', format(pv_1_7*0.5, '.2f').replace('.', ','))
        elif ds == 2 or ds == 3 or ds == 4:
                    print('Valor do ingresso: R$', format(pv_2_3_4*0.5, '.2f').replace('.', ','))
        elif ds == 5 or ds == 6:
                    print('Valor do ingresso: R$', format(pv_5_6*0.5, '.2f').replace('.', ','))
    else:
        if ds == 1 or ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.5, '.2f').replace('.', ','))
        elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3*0.5, '.2f').replace('.', ','))
        elif ds == 6 or ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7*0.5, '.2f').replace('.', ','))
else:
    if hs == 18:
        if ms >= 30:
            if mp == "D":
                if ds == 1 or ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3, '.2f').replace('.', ','))
                elif ds == 6 or ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7, '.2f').replace('.', ','))
            else:
                if ds == 1:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.7, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3*0.5, '.2f').replace('.', ','))
                elif ds == 6:
                    print('Valor do ingresso: R$', format(pn_6_7*0.7, '.2f').replace('.', ','))
                elif ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7*0.8, '.2f').replace('.', ','))
                elif ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.5, '.2f').replace('.', ','))
        else:
            if mp == "D":
                if ds == 1 or ds == 7:
                    print('Valor do ingresso: R$', format(pv_1_7, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3 or ds == 4:
                    print('Valor do ingresso: R$', format(pv_2_3_4, '.2f').replace('.', ','))
                elif ds == 5 or ds == 6:
                    print('Valor do ingresso: R$', format(pv_5_6, '.2f').replace('.', ','))
            else:
                if ds == 1:
                    print('Valor do ingresso: R$', format(pv_1_7*0.7, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3 or ds == 4:
                    print('Valor do ingresso: R$', format(pv_2_3_4*0.5, '.2f').replace('.', ','))
                elif ds == 5 or ds == 6:
                    print('Valor do ingresso: R$', format(pv_5_6*0.5, '.2f').replace('.', ','))
                elif ds == 7:
                    print('Valor do ingresso: R$', format(pv_1_7*0.8, '.2f').replace('.', ','))
    elif hs < 18:
        if mp == "D":
                if ds == 1 or ds == 7:
                    print('Valor do ingresso: R$', format(pv_1_7, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3 or ds == 4:
                    print('Valor do ingresso: R$', format(pv_2_3_4, '.2f').replace('.', ','))
                elif ds == 5 or ds == 6:
                    print('Valor do ingresso: R$', format(pv_5_6, '.2f').replace('.', ','))
        else:
            if ds == 1:
                        print('Valor do ingresso: R$', format(pv_1_7*0.7, '.2f').replace('.', ','))
            elif ds == 2 or ds == 3 or ds == 4:
                        print('Valor do ingresso: R$', format(pv_2_3_4*0.5, '.2f').replace('.', ','))
            elif ds == 5 or ds == 6:
                        print('Valor do ingresso: R$', format(pv_5_6*0.5, '.2f').replace('.', ','))
            elif ds == 7:
                        print('Valor do ingresso: R$', format(pv_1_7*0.8, '.2f').replace('.', ','))
    else:
        if mp == "D":
                if ds == 1 or ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3, '.2f').replace('.', ','))
                elif ds == 6 or ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7, '.2f').replace('.', ','))
        else:
                if ds == 1:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.7, '.2f').replace('.', ','))
                elif ds == 2 or ds == 3:
                    print('Valor do ingresso: R$', format(pn_2_3*0.5, '.2f').replace('.', ','))
                elif ds == 6:
                    print('Valor do ingresso: R$', format(pn_6_7*0.7, '.2f').replace('.', ','))
                elif ds == 7:
                    print('Valor do ingresso: R$', format(pn_6_7*0.8, '.2f').replace('.', ','))
                elif ds == 4 or ds == 5:
                    print('Valor do ingresso: R$', format(pn_1_4_5*0.5, '.2f').replace('.', ','))
        