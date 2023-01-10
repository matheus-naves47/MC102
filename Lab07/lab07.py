###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

# Leitura das tropas de defesa

n_def = int(input())

def_stats = []

for i in range(n_def):
  df_st = int(input())
  def_stats.append(df_st)

# Leitura das tropas de ataque

n_atq = int(input())

atq_stats = []

for j in range(n_atq):
  at_st = int(input())
  atq_stats.append(at_st)


# Processamento da guerra

resultados = []
posicoes = []

for ofs in range((len(def_stats) - len(atq_stats))):
  conf = list(zip(def_stats[ofs:], atq_stats))
  soma = [y-x for (x,y) in conf]
  resultados.append(soma)

res_final = []

for i in range(len(resultados)):
  vitorias = sum(map(lambda x : x > 0, resultados[i]))
  derrotas = sum(map(lambda x : x < 0, resultados[i]))
  empates = sum(map(lambda x : x == 0, resultados[i]))
  if vitorias > derrotas:
    res_final.append('Vitória')
  elif vitorias == derrotas:
    res_final.append('Derrota')
  else:
    res_final.append('Derrota')

# Saída de dados

if "Vitória" in res_final:
  posicao = list(x == 'Vitória' for x in res_final).index(True)
  print('Vitória posicionando as tropas a partir da posição', posicao + 1)
else:
  print('Derrota')
