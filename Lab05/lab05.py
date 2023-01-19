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
horas = []
horas_trabalhadas = []
horas_extras = []

for d in range(D):
    P = int(input(""))
    periodos.append(P)
    for p in range(P):
        horas_inicio.append(int(input("")))
        horas_final.append(int(input("")))
        
for final, inicial in zip(horas_final, horas_inicio):
    horas.append(abs(final - inicial))

t=0
horas_dia = []

for i in range(len(periodos)):
    h = t + periodos[i]
    h_dia = horas[t:h]
    t+=periodos[i]
    horas_trabalhadas.append(sum(h_dia))

for i in range(len(horas_trabalhadas)):
    if horas_trabalhadas[i] > 8:
        horas_extras.append(horas_trabalhadas[i] - 8)
    else:
        horas_extras.append(0)


horas_trabalhadas = sum(horas_trabalhadas)
horas_extras = sum(horas_extras)
excedente = (horas_trabalhadas - horas_extras) - 44 # horas não contadas como extra


# Cálculo do valor devido ao funcionário
if horas_trabalhadas > 44 and excedente >= 0:
    valor = (horas_trabalhadas*V) + horas_extras*(V/2) + (excedente * (V/2))
    horas_extras = horas_extras + excedente
elif horas_trabalhadas > 44 and excedente < 0:
    valor = (horas_trabalhadas*V) + horas_extras*(V/2)
elif horas_trabalhadas < 44 and excedente < 0:
    valor = (horas_trabalhadas*V) + horas_extras*(V/2)
else:
    valor = (horas_trabalhadas*V)


# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))