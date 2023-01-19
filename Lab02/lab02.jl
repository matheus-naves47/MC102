###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte (Julia)
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################
d_sx = parse(Int, readline()) # distância entre a Terra e Marte no lançamento da nave da SpaceX (km)
v_sx = parse(Int, readline()) # velocidade da nave da SpaceX (km/h)
t = parse(Int, readline()) # tempo(dias) entre o lançamento da SpaceX e Blue Origin
d_bo = parse(Int, readline()) # distância entre a Terra e Marte no lançamento da nave da Blue Origin (km)
v_bo = parse(Int, readline()) # velocidade da nave da Blue Origin (km/h)

# Cálculo do tempo total gasto por cada nave

t_sx = (d_sx / v_sx)/24 # tempo total da nave da SpaceX
t_bo = (d_bo / v_bo)/24 # tempo total da nave da Blue Origin

# impressão da resposta

if t_sx > t_bo + t
    println("False")
else
    println("True")
end