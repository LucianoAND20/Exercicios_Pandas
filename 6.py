import pandas as pd

df = pd.read_csv('aluguel.csv')

df['total'] = df['Valor'] + df['Condominio'] + df['ITPU']

estatisticas_descritivas = df.describe()

print(estatisticas_descritivas)
