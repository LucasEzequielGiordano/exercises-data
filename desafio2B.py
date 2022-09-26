import pandas as pd

df = pd.read_excel("Datos.xlsx")
records = df.to_dict('records')
print(df)
alumno = input('Ingrese un alumno: ')
for i in records:
    if i['Nombre'] == alumno:
        promedio = f"El promedio de las notas de {alumno} es de: {(i['Quimica'] + i['Fisica'] + i['Matematica']) / 3}"
        print(promedio)