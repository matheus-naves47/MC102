###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema (Julia)
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# leitura de dados

dia_semana = parse(Int, readline())
hora_inicio_sessao = parse(Int, readline())
min_inicio_sessao = parse(Int, readline())
estudante = readline()
metodo_pagamento = readline()


# valor do ingresso inteiro

# usar dicionário para guardar os valores inteiros
# uma chave pra cada dia_semana
# um dicionario para cada turno(vespertino, noturno)

valores_vespertino = Dict([("Domingo", 30), ("Segunda", 15), ("Terça", 15), ("Quarta", 15), ("Quinta", 20), ("Sexta", 20), ("Sabado", 30)])
valores_noturno = Dict([("Domingo", 30), ("Segunda", 20), ("Terça", 20), ("Quarta", 30), ("Quinta", 30), ("Sexta", 40), ("Sabado", 40)])
descontos_cc_vespertino = Dict([("Domingo", 0.7), ("Segunda", 0.5), ("Terça", 0.5), ("Quarta", 0.5), ("Quinta", 0.5), ("Sexta", 0.5), ("Sabado", 0.8)])
descontos_cc_noturno = Dict([("Domingo", 0.7), ("Segunda", 0.5), ("Terça", 0.5), ("Quarta", 0.5), ("Quinta", 0.5), ("Sexta", 0.7), ("Sabado", 0.8)])

# valor a pagar

function valor_ingresso(d, h, m, e, p)
    if e == "S"
        if h == 18
            if m >= 30
                if d == 1 | d == 4 | d == 5
                    valor = valores_noturno["Domingo"] + 1
                elseif d == 2 | d == 3
                    valor = valores_noturno["Segunda"] + 1
                else
                    valor = valores_noturno["Sexta"] + 1
                end
                println("Valor: ", valor)
            else
                if d == 1 | d == 7
                    valor = valores_vespertino["Domingo"] * 0.5
                elseif d == 2 | d == 3 | d == 4
                    valor = valores_vespertino["Segunda"] * 0.5
                else
                    valor = valores_vespertino["Quinta"] * 0.5
                end
                println("Valor: ", valor)
            end
        elseif h < 18
            if d == 1 | d == 7
                valor = valores_vespertino["Domingo"] * 0.5
            elseif d == 2 | d == 3 | d == 4
                valor = valores_vespertino["Segunda"] * 0.5
            else
                valor = valores_vespertino["Quinta"] * 0.5
            end
            println("Valor: ", valor)
        else
            if d == 1 | d == 4 | d == 5
                valor = valores_noturno["Domingo"] ÷ 2
            elseif d == 2 | d == 3
                valor = get(valores_noturno, "Segunda", 0) * 0.5
            else
                valor = valores_noturno["Sexta"] ÷ 2
            end
            println("Valor: ", valor)
        end   
    else
        if h == 18
            if m >= 30
                if p == "D"
                    if d == 1 | d == 4 | d == 5
                        valor = valores_noturno["Domingo"]*0.5
                    elseif d == 2 | d == 3
                        valor = valores_noturno["Segunda"]*0.5
                    else
                        valor = valores_noturno["Sexta"]*0.5
                    end
                else
                    if d == 1
                        valor = valores_noturno["Domingo"]*0.7
                    elseif d == 2 | d == 3
                        valor = valores_noturno["Segunda"]*0.5
                    elseif d == 4 | d == 5
                        valor = valores_noturno["Quarta"]*0.5
                    elseif d == 6
                        valor = valores_noturno["Sexta"]*0.7
                    else
                        valor = valores_noturno["Sabado"]*0.8
                    end
                end
            else
                if p == "D"
                    if d == 1 | d == 7
                        valor = valores_vespertino["Domingo"]
                    elseif d == 2 | d == 3 | d == 4
                        valor = valores_vespertino["Segunda"]
                    else
                        valor = valores_vespertino["Quinta"]
                    end
                else
                    if d == 1
                        valor = valores_vespertino["Domingo"]*0.7
                    elseif d == 2 | d == 3 | d == 4
                        valor = valores_vespertino["Segunda"]*0.7
                    elseif d == 5 | d == 6
                        valor = valores_vespertino["Quinta"]*0.5
                    else
                        valor = valores_vespertino["Sabado"]*0.8
                    end
                end
            end
        elseif h < 18
            if p == "D"
                if d == 1 | d == 7
                    valor = valores_vespertino["Domingo"]
                elseif d == 2 | d == 3 | d == 4
                    valor = valores_vespertino["Segunda"]
                else
                    valor = valores_vespertino["Quinta"]
                end
            else
                if d == 1
                    valor = valores_vespertino["Domingo"]*0.7
                elseif d == 2 | d == 3 | d == 4
                    valor = valores_vespertino["Segunda"]*0.5
                elseif d == 5 | d == 6
                    valor = valores_vespertino["Quinta"]*0.5
                else
                    valor = valores_vespertino["Sabado"]*0.8
                end
            end
        else
            if p == "D"
                if d == 1 | d == 4 | d == 5
                    valor = valores_noturno["Domingo"]
                elseif d == 2 | d == 3
                    valor = valores_noturno["Segunda"]
                else
                    valor = valores_noturno["Sexta"]
                end
            else
                if d == 1
                    valor = valores_noturno["Domingo"]*0.7
                elseif d == 2 | d == 3
                    valor = valores_noturno["Segunda"]*0.5
                elseif d == 4 | d == 5
                    valor = valores_noturno["Quarta"]*0.5
                elseif d == 6
                    valor = valores_noturno["Sexta"]*0.7
                else
                    valor = valores_noturno["Sabado"]*0.8
                end

            end
        end
    end
end





    



valor_ingresso(dia_semana, hora_inicio_sessao, min_inicio_sessao, estudante, metodo_pagamento)


println(valores_noturno["Segunda"])


# # saída do valor do ingresso

# println("Valor do ingresso: R💲", ingresso) # , format(ingresso, '.2f').replace('.', ','))

        