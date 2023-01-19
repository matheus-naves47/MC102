##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho (Julia)
# Nome: Matheus Alves de Andrade
# RA: 256296
##################################################

# Leitura do valor da hora
valor_hora = parse(Int, readline())

# Leitura do numero de dias trabalhados na semana
dias_trabalhados = parse(Int, readline())

# Leitura e processamento dos periodos de trabalho de cada dia
horas_inicio = []
horas_final = []
periodos = []
horas = []
horas_trabalhadas = []
horas_extras = []



for d in range(1, stop = dias_trabalhados)
    P = parse(Int, readline())
    push!(periodos, P)
    for p in range(1, stop = P)
        push!(horas_inicio, parse(Int, readline()))
        push!(horas_final, parse(Int, readline()))
    end
end
        
for (final, inicial) ∈ zip(horas_final, horas_inicio)
    push!(horas, abs(final - inicial))
end

t = 1
horas_dia = []

for i in range(1, stop = length(periodos))
    h = t + periodos[i]
    h_dia = horas[Int(t):Int(h-1)]
    global t+=periodos[i]
    push!(horas_trabalhadas, sum(h_dia))    
end

for i in range(1, stop = length(horas_trabalhadas))
    if horas_trabalhadas[i] > 8
        push!(horas_extras, horas_trabalhadas[i] - 8)
    else
        push!(horas_extras, 0)
    end
end


horas_trabalhadas = sum(horas_trabalhadas)
horas_extras = sum(horas_extras)
excedente = (horas_trabalhadas - horas_extras) - 44 # horas não contadas como extra


# Cálculo do valor devido ao funcionário
if horas_trabalhadas > 44 && excedente >= 0
    valor = (horas_trabalhadas * valor_hora) + (horas_extras * (valor_hora / 2)) + (excedente * (valor_hora / 2))
    horas_extras = horas_extras + excedente
    return valor
elseif horas_trabalhadas > 44 && excedente < 0
    valor = (horas_trabalhadas * valor_hora) + (horas_extras * (valor_hora / 2))
    return valor
elseif horas_trabalhadas < 44 && excedente < 0
    valor = (horas_trabalhadas * valor_hora) + (horas_extras * (valor_hora / 2))
    return valor
else
    valor = (horas_trabalhadas * valor_hora)
    return valor
end


# Impressão da saída
println("Horas trabalhadas: ", horas_trabalhadas)
println("Horas extras: ", horas_extras)
println("Valor devido: R\$ ", Float64(valor), 0)