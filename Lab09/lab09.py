###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Matheus Alves de Andrade
# RA: 256296
###################################################

import pandas as pd

# Leitura de dados

dados = pd.DataFrame(columns=['Produto', 'Estoque', 'Pedidos', 'Compras', 'Vendas'])

while True:
    try:
        N, X = input().split(" : ")
        X = int(X)
        dados = dados.append(dict({'Produto' : N, 'Estoque' : 0, 'Pedidos' : X, 'Compras' : 0, 'Vendas' : 0}), ignore_index=True)
    
    except ValueError:
        break

# order = dados.drop_duplicates(subset='Produto')

# Processamento

for i in dados.index:
    for j in range(0,i):
        if dados.iloc[j,0] == dados.iloc[i,0]:
            dados.iloc[i,1] = dados.iloc[j,1]
    if dados.iloc[i,2] > 0:
        dados.iloc[i,3] =+1
        dados.iloc[i,1] = dados.iloc[i,2]
    elif dados.iloc[i,2] < 0 and abs(dados.iloc[i,2]) <= dados.iloc[i,1]:        
        dados.iloc[i,4] =+1
        dados.iloc[i,1] = dados.iloc[i,1] + dados.iloc[i,2]
    elif dados.iloc[i,2] < 0 and abs(dados.iloc[i,2]) > dados.iloc[i,1]:
        print("Quantidade indisponivel para a venda de " + str(abs(dados.iloc[i,2])) + " unidade(s) do produto " + dados.iloc[i,0] + ".")
    
dados[['Compras', 'Vendas']] = dados.groupby(['Produto'])['Compras', 'Vendas'].transform('sum')
dados[['Estoque']] = dados.groupby(['Produto'])['Estoque'].transform('last')
# dados['Estoque'] = dados['Estoque'].clip(lower=0)


dados.drop_duplicates(subset='Produto', inplace=True)
dados.reset_index(inplace=True, drop=True)

print(dados)

# dados = dados.sort_values(by='Produto', ascending=True)

for i in dados.index:
    if dados.iloc[i,3] + dados.iloc[i,4] > 0:
        print("Produto: " + str(dados.iloc[i,0]))
        print("Quantidade em Estoque: " + str(dados.iloc[i,1]))
        print("Pedidos de Compra: " + str(dados.iloc[i,3]))
        print("Pedidos de Venda: " + str(dados.iloc[i,4]))

        
         