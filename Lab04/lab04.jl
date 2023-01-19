###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque (Julia)
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# leitura da sequência de compras e vendas
estoque = 0
vendas = 0

while true
    x = parse(Int, readline())
    if x > 0
        estoque = estoque + x
        continue
    elseif x < 0
        if estoque - abs(x) < 0
            println("Quantidade indisponível para a venda de ", string(abs(x)), " unidades.")
            continue
        else
            global estoque = estoque - abs(x)
            global vendas += 1
            continue
        end
    else
        println("Quantidade de vendas realizadas: ", string(vendas))
        println("Quantidade em estoque: ", string(estoque))
        break
    end
end

