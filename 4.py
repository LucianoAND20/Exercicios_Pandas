import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7])

resultado = s1 + s2

print(resultado)

resultado_tratado = resultado.fillna(0)

print("\nDepois do FIilna:")
print(resultado_tratado)
