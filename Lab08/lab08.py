###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# Leitura da palavra
word = str(input())

# Leitura dos palpites e impressão do resultado para cada palpite

guess_check = []
for i in word:
    guess_check.append("")
    

tries = 1

while tries <=6:
    guess = str(input())
    for i, l in enumerate(guess):
        if guess[i] in word and guess[i] == word[i]:
            guess_check[i] = guess[i].upper()
        elif guess[i] in word and guess[i] != word[i]:
            guess_check[i] = guess[i]
        elif guess[i] not in word:
            guess_check[i] = "_"
    print(''.join(guess_check))
    tries = tries + 1
    if ''.join(guess_check) == word.upper():
        print("Resposta correta")
        break
    elif tries == 7 and ''.join(guess_check) != word.upper():
        print("Palavra correta:", word)



