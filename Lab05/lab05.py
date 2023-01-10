##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Matheus Alves de Andrade
# RA: 256296
##################################################

# Leitura do valor da hora
V = int(input(""))

# Leitura do numero de dias trabalhados na semana
D = int(input(""))


# Leitora e processamento dos periodos de trabalho de cada dia
horas_inicio = []
horas_final = []
periodos = []
horas_trabalhadas = []
horas_extras = []

for d in range(D):
    P = int(input(""))
    periodos.append(P)
    for p in range(P):
        horas_inicio.append(int(input("")))
        horas_final.append(int(input("")))


        
for final, inicial in zip(horas_final, horas_inicio):
    horas_trabalhadas.append(abs(final - inicial))

t=0
horas_trabalhadas_pd = []

for i in range(len(periodos)):
    h = t+periodos[i]
    hts = horas_trabalhadas[t:h]
    t+=periodos[i]
    hex = sum(hts)
    horas_extras.append(hex)
    horas_trabalhadas_pd.append(sum(hts))



horas_extras = [h - 8 for h in horas_extras]

for i in range(len(horas_extras)):
    if horas_extras[i] < 0:
        horas_extras[i] = 0


extra_m_dia = []
for trabalhadas, extras in zip(horas_trabalhadas_pd, horas_extras):
    extra_m_dia.append(abs(trabalhadas - 8))

extra_m_dia = sum(extra_m_dia)

horas_trabalhadas = sum(horas_trabalhadas)

horas_extras = [h-8 for h in horas_trabalhadas_pd if h > 8]
horas_extras = sum(horas_extras)

# print(horas_trabalhadas)
# print(horas_trabalhadas_pd)
# print(horas_extras)

# Calculo do valor devido ao funcionário

if sum(horas_trabalhadas_pd) > 44:
    horas_extras = horas_trabalhadas-44
    valor = (horas_trabalhadas*V) + horas_extras*(V/2)
    print("Horas trabalhadas:", horas_trabalhadas)
    print("Horas extras:", horas_extras)
    print("Valor devido: R$ {:0.2f}".format(valor))
else:
    valor = (horas_trabalhadas*V) + horas_extras*(V/2)
    print("Horas trabalhadas:", horas_trabalhadas)
    print("Horas extras:", horas_extras)
    print("Valor devido: R$ {:0.2f}".format(valor))
