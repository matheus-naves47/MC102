###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 1 - Aritmética com Inteiros (Julia)
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

a = parse(BigInt, readline())
b = parse(BigInt, readline())

begin
    println("a = ", a)
    println("b = ", b)
    println("a + b = ", a + b)
    println("a - b = ", a - b)
    println("a * b = ", a * b)
    println("a ** b = ", a ^ b)
    println("a // b = ", a ÷ b)
    println("a % b = ", a % b)
end
