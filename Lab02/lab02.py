###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# Leitura de dados

d_sx = int(input())
v_sx = int(input())
t = int(input())
d_bo = int(input())
v_bo = int(input())



# Cálculo do tempo total gasto por cada espaçonave 

t_sx = (d_sx/v_sx)/24
t_bo = (d_bo/v_bo)/24

# Impressão da resposta

if t_sx > t_bo + t:
    print("False")
else:
    print("True")
