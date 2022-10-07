import pandas as pd

listas = [ "lista1.csv", "lista2.csv" ]

clientes = dict() 

todosloscampos = set()


for lista in listas: 
    archivo = pd.read_csv(lista, index_col =["Mail"])
    data = archivo.to_dict("index") 
    
    print("Base de datos", lista)
    print(archivo)

    for mail in data: 
        if mail not in clientes: 
            clientes[mail] = dict() 
        
        campos = data[mail]

        for campo in campos:
            clientes[mail][campo] = data[mail][campo]
            todosloscampos.add(campo)

    print("  ")
    
df = pd.DataFrame.from_dict(clientes, orient='index')
print("Base de datos unificada")
print(df)

df.to_csv('listafinal.csv')