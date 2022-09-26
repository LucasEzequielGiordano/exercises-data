import pandas as pd

df = pd.read_excel("Tabla1.xlsx")
sort = df.sort_values('Puntos', ascending=False)
points = sort.to_dict('records')

print('Los equipos que obtuvieron puntaje mayor a 20 pts de forma descendiente')
for n in points:
    if n['Puntos'] > 20:
        print(f"Equipo: {n['Equipo']}. Puntos: {int(n['Puntos'])}, Goles a favor: {int(n['Goles a favor'])}, Goles en contra: {int(n['Goles en contra'])}")