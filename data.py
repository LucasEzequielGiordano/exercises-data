import pandas as pd

df = pd.read_csv('full_data.csv')
pd.set_option('display.max_columns', 10)

# print(df)
# print(df.shape)
# print(df.size)
# print(df.info())
# print(df['new_cases'].sum() / 2, df['total_cases'].max())

df = df[df['location'] != 'World']

# print(df[df['new_cases'] == df['new_cases'].max()])
print(df[(df['new_cases'] >3000) | (df['total_cases'] < 2000 )])