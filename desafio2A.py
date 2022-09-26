import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

notas = df['Quimica']
promedio = sum(notas)
print(promedio / 6)