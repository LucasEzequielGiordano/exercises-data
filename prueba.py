import pandas as pd
import random as n 

data = {
    'Usuario': ['Lucas', 'Ezequiel', 'Giordano'],
    'Password': ['abc123', 'contrasegura', '123cba'],
    'Random': []
}

for i in range(3):
    data['Random'].append( n.randint(1,30) )

print(data)

df = pd.DataFrame(data)

print(df['new_cases'].sum())
print(df['total_cases'].max())