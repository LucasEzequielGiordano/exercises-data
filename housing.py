import pandas as pd
import numpy as np

df = pd.read_excel("california_housing_train.xlsx") 

#Pregunta 1 y 2 (utilizando filtrado)
ans = 0
hab = 0
filtro_lon = (-120 <= df['longitude']) & (df['longitude'] <= -118)
filtro_val = df['median_house_value'] > 80000
ans = len( df[filtro_lon & filtro_val] )
hab = sum(df[filtro_lon & filtro_val]['total_rooms'])
print(ans)
print(hab/ans)

#Pregunta 1 y 2 (sin utilizar filtrado)
ans = 0
hab = 0
for i,lon in enumerate(df['longitude']):
    if -120 <= lon and lon<=-118 :
        if df['median_house_value'][i] > 80000:
            ans+=1
            hab+=df['total_rooms'][i]
print(ans)
print(hab/ans)

#Pregunta 3
m = max(df['median_house_value'])
c = sum(df['median_house_value'] == m)
print(m)
print(c)

#pregunta 4
m = np.mean(df['median_house_value'])
v = np.var(df['median_house_value'])
print(m)
print(v)