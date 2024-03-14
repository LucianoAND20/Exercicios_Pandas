import pandas as pd

# Criando as séries
s1 = pd.Series([1, 2, 3, 4], index=['abroba', 'bacate', 'cabaxi', 'doom'])
s2 = pd.Series([5, 6, 7], index=['bacate', 'cabaxi', 'abroba'])


resultado = s1 - s2

print("Resultado da subtração:")
print(resultado)
