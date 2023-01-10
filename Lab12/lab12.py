###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))


def expansao(imagem_original):

    imagem_redim = [[0 for i in range(2*m - 1)] for j in range(2*n - 1)]

    for i in range(n):
        for j in range(m):
            if not(i == 0 and j == 0):
                    imagem_redim[i*2][j*2] = imagem_original[i][j]
            else:
                    imagem_redim[0][0] = imagem_original[0][0]

    for i in range(2*n - 1):
            for j in range(2*m - 1):
                if j % 2 != 0 and i % 2 == 0:
                    imagem_redim[i][j] = (imagem_redim[i][j-1] + imagem_redim[i][j+1])/2

    for i in range(2*n - 1):
            for j in range(2*m - 1):
                if i % 2 != 0 and j % 2 == 0:
                    imagem_redim[i][j] = (imagem_redim[i-1][j] + imagem_redim[i+1][j])/2

    for i in range(2*n - 1):
            for j in range(2*m - 1):
                if j % 2 != 0 and i % 2 != 0:
                    imagem_redim[i][j] = (imagem_redim[i-1][j-1] + imagem_redim[i-1][j+1] + imagem_redim[i+1][j-1] + imagem_redim[i+1][j+1])/4


    imprimir_imagem(imagem_redim)


def teto(x):
    if x % 2 == 0:
        return int(x/2)
    else:
        return int((x+1)/2)


def retracao(imagem_original):
    
    imagem_redim  = [[0 for i in range(teto(m))] for j in range(teto(n))]

    l = max(0, n - 1)
    k = max(0, m - 1)

    if (m % 2 != 0) and (n % 2 == 0):
        for s in range(0, teto(l)):
            i = 2*s
            imagem_redim[s][teto(m) - 1] = (imagem_original[i][m - 1] + imagem_original[i + 1][m - 1])/2

    if (n % 2 != 0) and (m % 2 == 0):
        for s in range(0, teto(k)):
            i = 2*s
            imagem_redim[teto(n) - 1][s] = (imagem_original[n - 1][i] + imagem_original[n - 1][i + 1])/2


    if (n % 2 != 0) and (m % 2 != 0):
        imagem_redim[teto(n) - 1][teto(m) - 1] = imagem_original[n-1][m-1]
        l = max(0, n - 1)
        for s in range(0, teto(l)):
            i = 2*s
            imagem_redim[s][teto(m) - 1] = (imagem_original[i][m - 1] + imagem_original[i + 1][m - 1])/2


        k = max(0, m - 1)
        for s in range(0, teto(k)):
            i = 2*s
            imagem_redim[teto(n) - 1][s] = (imagem_original[n - 1][i] + imagem_original[n - 1][i + 1])/2


    for s in range(teto(l)):
        for t in range(teto(k)):
            i = 2*s
            j = 2*t
            imagem_redim[s][t] = (imagem_original[i][j] + imagem_original[i+1][j] + imagem_original[i][j+1] + imagem_original[i+1][j+1])/4

    imprimir_imagem(imagem_redim)



# leitura da imagem
ign = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

ign = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)




# leitura do tipo de redimensionamento

tipo_red = str(input())


if tipo_red == 'expansao':
    expansao(imagem_original)
else:
    retracao(imagem_original)