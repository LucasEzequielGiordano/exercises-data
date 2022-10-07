import pandas as pd
import numpy as np

archivo = pd.read_excel("california_housing_train.xlsx") 
paso = .5

lats = np.arange(32.5,42.5,paso)
lons = np.arange(-124.3,113.3,paso) 
maximoValor = 0
maximaLat = 0
maximaLon = 0
for lat in lats:
    for lon in lons:
        data = archivo[(archivo['latitude']>=lat) & (archivo['latitude']<=lat+paso)]
        data = data[(data['longitude']>=lon) & (data['longitude']<=lon+paso)]
        if(len(data)>100):
            m = np.mean(data['median_house_value'])
            if m > maximoValor:
                maximaLat = lat
                maximaLon = lon
                maximoValor = m
                
print('Latitude:',maximaLat,'Longitude',maximaLon,'Price',maximoValor)