import pandas as pd

df = pd.read_excel("Tabla1.xlsx")
sort =  df.sort_values('Puntos', ascending=False)
records = sort.to_dict('records')

print(f"Campeón: {records[0]['Equipo']} - Puntos: {int(records[0]['Puntos'])}")
print(f"Último: {records[-1]['Equipo']} - Puntos: {int(records[-1]['Puntos'])}")