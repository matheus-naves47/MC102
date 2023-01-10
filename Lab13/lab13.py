###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# Leitura de dados

# lista_votacao = [voto for voto in input()]

# Saída de dados

# print(lista_votacao)

lista_votacao = []
lista_votacao_b_n = []
voto = None

while (voto != "0"):
    voto = str(input(""))
    if voto != "0":
        try:
            if voto == 'Branco' or voto == 'Nulo':
                lista_votacao_b_n.append(str(voto))
            else:
                lista_votacao.append(str(voto))
        except:
            break

# for i in range(len(lista_votacao)):
#     print(lista_votacao[i])

dict_votacao = {}
for voto in lista_votacao:
    dict_votacao[voto] = dict_votacao.get(voto, 0) + 1

dict_votacao_b_n = {}
for voto in lista_votacao_b_n:
    dict_votacao_b_n[voto] = dict_votacao_b_n.get(voto, 0) + 1
    

votos = sorted(dict_votacao.items(), key=lambda x: x[1], reverse=True)
votos_b_n = sorted(dict_votacao_b_n.items(), key=lambda x: x[0], reverse=False)


for i in votos:
	print(i[0], i[1])

for j in votos_b_n:
    if j[0] == 'Branco':
        print('Brancos', j[1])
    else:
        print('Nulos', j[1])