import pandas as pd
# import numpy as np

df = pd.read_csv("recorridos-realizados-2021-sample.csv") 
print(df)
numero_de_filas = len(df)

estado_count = df['Estado cerrado'].value_counts()
porcentaje_normal = 100*(estado_count['NORMAL'] / numero_de_filas)
print(f'El {porcentaje_normal:.2f}% de los viajes se completaron en estado NORMAL')

duracion_promedio = round(df['Duración'].mean())
print(f'La duración promedio es de {duracion_promedio//60} minutos {duracion_promedio%60} segundos')

horarios_de_inicio = df['Fecha de inicio']
horarios_de_inicio = pd.to_datetime(horarios_de_inicio)
horas_de_inicio = horarios_de_inicio.dt.hour
hora_pico = horas_de_inicio.value_counts().idxmax()
print(f'La hora más concurrida es de {hora_pico}hs a {hora_pico+1}hs')

estaciones_inicio = df['Nombre de estación de inicio']
estaciones_fin = df['Nombre de estación de fin de viaje']
estaciones_total = pd.concat([estaciones_inicio, estaciones_fin])
print(f'Se utilizaron {len(estaciones_total.value_counts())} estaciones en total')

print('\nCantidad de viajes iniciados en cada estación:\n')
for estacion, cantidad in estaciones_inicio.value_counts().iteritems():
  print('Cantidad:', cantidad, ' Estación:', estacion)