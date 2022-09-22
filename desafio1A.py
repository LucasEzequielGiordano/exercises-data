import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")
records = df.to_dict('records')
for i in records:
    print(i['Equipo'], ' - ' ,int(i['Goles a favor']) - int(i['Goles en contra']))