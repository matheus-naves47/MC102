#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Matheus Alves de Andrade
# RA: 256296
#####################################################

# Leitura da matriz

n = int(input())
sala = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos

primeiro_time = str(input())
jogadores = int(input())

caminhos = []

for i in range(0, jogadores):
    caminho = list(str(input()))
    caminhos.append(caminho)

X = []
Y = []

pos_i = 0
pos_j = 0

if primeiro_time == 'azul':
    X.append(sala[0][0])
else:
    Y.append(sala[0][0])
     


for i in range(len(caminhos)):
    if primeiro_time == 'azul' and i % 2 == 0:
        for j in range(len(caminhos[i])):
            if caminhos[i][j] == 'N':
                pos_i = pos_i - 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'S':
                pos_i = pos_i + 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'L':
                pos_j = pos_j + 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'O':
                pos_j = pos_j - 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
        pos_i = 0
        pos_j = 0
    elif primeiro_time == 'vermelho' and i % 2 == 0:
        for j in range(len(caminhos[i])):
            if caminhos[i][j] == 'N':
                pos_i = pos_i - 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'S':
                pos_i = pos_i + 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'L':
                pos_j = pos_j + 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'O':
                pos_j = pos_j - 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
        pos_i = 0
        pos_j = 0
    elif primeiro_time == 'azul' and i % 2 != 0:
        for j in range(len(caminhos[i])):
            if caminhos[i][j] == 'N':
                pos_i = pos_i - 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'S':
                pos_i = pos_i + 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'L':
                pos_j = pos_j + 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'O':
                pos_j = pos_j - 1
                Y.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
        pos_i = 0
        pos_j = 0
    elif primeiro_time == 'vermelho' and i % 2 != 0:
        for j in range(len(caminhos[i])):
            if caminhos[i][j] == 'N':
                pos_i = pos_i - 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'S':
                pos_i = pos_i + 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'L':
                pos_j = pos_j + 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
            elif caminhos[i][j] == 'O':
                pos_j = pos_j - 1
                X.append(sala[pos_i][pos_j])
                if sala[pos_i][pos_j] == '*':
                    sala[pos_i][pos_j] = '.'
        pos_i = 0
        pos_j = 0

X = len([x for x in X if x == '*'])
Y = len([y for y in Y if y == '*'])

# Impressão da saída

print('Tesouros encontrados pelo time azul:', X)
print('Tesouros encontrados pelo time vermelho:', Y)

if X > Y:
    print('Vitoria do time azul')
elif X < Y:
    print('Vitoria do time vermelho')
else:
    print('Empate')