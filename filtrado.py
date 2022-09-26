import pandas as pd

df = pd.read_excel('Datos2.xlsx')

# obtener las notas existentes en Matematica
datos_matematica = df[(df['Matematica'].notna()) & (df['Matematica'] != 'A')]
datos_matematica = datos_matematica['Matematica']
print(datos_matematica)