##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Matheus Alves de Andrade
# RA: 256296
##################################################

# Leitura da torre de panquecas

torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
while True:
    M = int(input())
    if M == 0:
        break
    else:
        torre = torre[:M][::-1] + torre[M:]
        

# print('outputs: ')
# print(torre)
# print(sorted(torre))
# print(sorted(torre, reverse=True))

# Impressão da saída
if torre == sorted(torre):
    print("Torre estavel")
else:
    print("Torre instavel")