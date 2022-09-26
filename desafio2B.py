import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")
records = df.to_dict('records')

alumno = input('Ingrese un alumno: ')
for i in records:
    if i['Nombre'] == alumno:
        promedio = f"El promedio de las notas de {alumno} es de: {(i['Quimica'] + i['Fisica'] + i['Matematica']) / 3}"
        print(promedio)