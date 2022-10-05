# import numpy as np
# import pandas as pd

# table = np.array([[4, 6, 5], [8, 8, 8], [5, 7, 8]])
# df = pd.DataFrame(table, columns=['Matematica', 'Fisica', 'Quimica'])

# df2 = pd.DataFrame(df, columns=['Quimica', 'Matematica'])
# df2.to_excel('Alumnos.xlsx')

# import pandas as pd 
# tabla = pd.read_excel('LigaArgentina.xlsx')
# lista = tabla[tabla['Partidos']!= tabla['Partidos'].max()]
# print(lista['Equipo'])

# import pandas as pd 
# tabla = pd.read_excel('LigaArgentina.xlsx', index_col='Equipo')
# dataFrame = tabla.to_dict('index')
# print(dataFrame['Boca Juniors']['Puntaje'])

# import pandas as pd 
# tabla = pd.read_excel('LigaArgentina.xlsx')
# error = tabla[tabla['Goles convertidos'] - tabla['Goles recibidos']!=tabla['Diferencia de Gol']]
# print(error['Equipo'])

# import pandas as pd 
# tabla = pd.read_excel('Archivo.xlsx', index_col='Apellido')
# dataFrame = tabla.to_dict('index')
# print(dataFrame['Lopez']['Matemática'])

# import pandas as pd 
# tabla = pd.read_excel('LigaArgentina.xlsx', index_col='Equipo')
# tabla.loc[['Vélez Sarfield', 'Boca Juniors', 'River Plate', 'Estudiantes'], ['Partidos']] = 14

# # print(tabla.loc[tabla['Partidos'] != 14, ['Puntaje']])
# import matplotlib.pyplot as plt
# # import matplotlib as plt
# import numpy as np

# alpha = 0
# N = 25
# mu = [-10, 10]
# cxy = 3
# s = (10 * np.random.rand(N))**2
# x, y = np.random.multivariate_normal(mu, N).T
# plt.scatter(x, y, s=s, alpha=alpha)
# # plt.plot()
# plt.show()

# import pandas as pd
# tabla = pd.read_csv('tested.csv')
# print(tabla['Pclass'].value_counts(normalize=True, ascending=True))
# import matplotlib.pyplot as plt
# import numpy as np

# mu = [0, 0]                          # Valores medios de x e y
# cxy = [[1, 1], [1, 2]]               # Matriz de covarianza, [[Cxx, Cxy], [Cyx, Cyy]]
# x, y = np.random.multivariate_normal(mu, cxy, 5000).T
# s = (10 * np.random.rand(5000))**2
# plt.scatter(x, y, s=s, alpha=0.5)
# plt.show()
