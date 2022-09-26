import pandas as pd

df = pd.read_excel("Tabla1.xlsx")
records = df.to_dict('records')
for i in records:
    print(f"Equipo: {i['Equipo']}, Diferencia Gol: {int(i['Goles a favor']) - int(i['Goles en contra'])}")