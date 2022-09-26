import pandas as pd

df = pd.read_excel("Datos.xlsx")
print("Datos:\n")
print(df)

# aprobaron 
aprobados = df[ df['Quimica'] >= 4 ] 
print("\nAprobados en Química:\n")
print(aprobados)

# desaprobaron
reprobados = df[ (df['Quimica'] < 4) | (df['Matematica'] < 4) | (df['Fisica'] < 4) ]
print("Reprobaron al menos una materia:")
print(reprobados)