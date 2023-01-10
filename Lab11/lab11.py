#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome:
# RA:
#####################################################


'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Processamento

# Impressão do resultado
