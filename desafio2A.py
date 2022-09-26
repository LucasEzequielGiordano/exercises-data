import pandas as pd

df = pd.read_excel("Datos.xlsx")

notas = df['Quimica']
promedio = sum(notas)
print(promedio / 6)