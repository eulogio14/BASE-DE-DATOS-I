import pandas as pd

df = pd.read_csv('WorldCupMatches.csv')
print(' ¿En cuales mundiales ha participado variable?')
pais = input('Ingrese el nombre del país: ')
participaciones = df[(df['Home Team Name'] == pais) | (df['Away Team Name'] == pais)]['Year'].astype(int).unique()
print(f'El país {pais} ha participado en los siguientes mundiales: {participaciones}')
df2 = pd.read_csv('WorldCups.csv')
ListaDeMundiales = []
for year in participaciones:
    copa = df2[df2['Year'] == year]['Country'].values[0]
    print(f'En el mundial de {year}, la copa se jugó en {copa}.')
    ListaDeMundiales.append(copa + f' {year}')
    
print(ListaDeMundiales)