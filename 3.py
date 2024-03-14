import pandas as pd

dados_vendas = {
    'Produto1': pd.Series([10, 20, 15, 25, 30, 10, 5], index=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']),
    'Produto2': pd.Series([5, 8, 12, 18, 20, 10, 7], index=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']),
    'Produto3': pd.Series([15, 10, 5, 8, 12, 20, 25], index=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])
}

df_vendas = pd.DataFrame(dados_vendas)

print(df_vendas)
