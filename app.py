import pandas as pd
import numpy as np

df_transacoes = pd.read_csv('transacoes.csv')
df_transacoes = df_transacoes.fillna(df_transacoes.median)
print(df_transacoes)
