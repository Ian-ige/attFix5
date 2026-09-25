import pandas as pd
import numpy as np
from datetime import date
# Requisitos do Exercício (Passo a Passo):Ingestão, Performance e Limpeza:
df_transacoes = pd.read_csv('transacoes.csv')
df_transacoes['valor'] = df_transacoes['valor'].fillna(df_transacoes.median)
df_transacoes['plataforma'] = 'Mobile'
print(df_transacoes)

# Engenharia de Dados & Alinhamento Temporável:
dias_traducao = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}
df_transacoes['data_transacao'] = pd.to_datetime(df_transacoes['data_transacao']).dt.tz_localize('America/Sao_Paulo')
df_transacoes['mes'] = df_transacoes['data_transacao'].dt.month
df_transacoes['dia_da_semana'] = df_transacoes['data_transacao'].dt.day_name().map(dias_traducao)
df_transacoes = df_transacoes.drop_duplicates()
print(df_transacoes)

# Operações Vetorizadas e Filtros Bitwise:
df_transacoes["valor"] = pd.to_numeric(df_transacoes["valor"], errors="coerce")
df_transacoes_setembro = df_transacoes[
    (df_transacoes["mes"] == 9) &
    (
        (df_transacoes["estado_cliente"] == "SP") |
        (df_transacoes["estado_cliente"] == "RJ")
    ) &
    (df_transacoes["valor"] > 5000)
]

print(df_transacoes_setembro)