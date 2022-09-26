import pandas as pd

df = pd.read_excel('Datos.xlsx')
datos_matematica = df[(df['Matematica'] >= 6)]
datos = datos_matematica.to_dict('records')

for prom in datos:
    print(f"El promedio de notas de {prom['Nombre']} es de: {round((prom['Quimica'] + prom['Matematica'] + prom['Fisica']) / 3, 2)}")