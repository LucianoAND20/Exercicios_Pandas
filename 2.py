import pandas as pd

dados = {
    'Nome': ['Etoh', 'Cacique', 'Cabrito'],
    'Idade': [20, 22, 21],
    'Nota': [8, 7, 9]
}

df_alunos = pd.DataFrame(dados)

print(df_alunos)
