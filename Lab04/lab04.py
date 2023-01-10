###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# leitura da sequência de compras e vendas
estoque = 0
vendas = 0

while True:
    x = int(input(""))
    if x > 0:
            estoque = estoque + x
            continue
    elif x < 0:
        if estoque - abs(x) < 0:
            print("Quantidade indisponível para a venda de " + str(abs(x)) + " unidades.")
            continue
        else:
            estoque = estoque - abs(x)
            vendas += 1
            continue
    else:
            print("Quantidade de vendas realizadas: " + str(vendas))
            print("Quantidade em estoque: " + str(estoque))
            break
        