#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome:
# RA:
#####################################################

"""
Esta função recebe como parâmetro uma matriz que representa o tabuleiro,
uma posição atual (linha_atual, coluna_atual) no tabuleiro, uma posição 
final (linha_fim, coluna_fim) desejada e o parâmetro cor indica a cor da
última posição visitada no caminho.
O retorno esperado para a função é um valor booleano, com True indicando 
que foi possível encontrar um caminho e False indicando que não existe um
caminho.
"""

def caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor):


# Leitura dos dados

L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

# Verificação se existe um caminho

#
  print("caminho encontrado")
#
  print("caminho nao encontrado")
