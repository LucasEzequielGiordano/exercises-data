import pandas as pd

usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios",index_col="Usuario") 

print("Usuarios:")
print(usuarios_archivo)
print(" ")
usuarios = usuarios_archivo.to_dict("index")

transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")
transferencias = transferencias_archivo.to_dict("records")

print("Transferencias:")
print(transferencias_archivo)
print(" ")

for transferencia in transferencias: 
    emisor = transferencia["Emisor"]
    receptor = transferencia["Receptor"]
    monto = transferencia["Monto"]

    usuarios[emisor]["Presupuesto"] -= monto
    usuarios[receptor]["Presupuesto"] += monto

usuarios_actualizados = pd.DataFrame.from_dict(usuarios, orient="index")
print("Usuarios luego de realizar las transferencias:")
print(usuarios_actualizados)

usuarios_actualizados.to_excel("usuarios_actualizados.xlsx")