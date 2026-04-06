import pandas as pd

df = pd.read_csv('WorldCupMatches.csv')
print('¿Cuántas veces se enfrentaron A y B en los mundiales?')
A = input('Ingrese el nombre del país A:')
B = input('Ingrese el nombre del país B:')
print(f"BUSCANDO Cuántas veces se enfrentaron {A} y {B} en los mundiales?")
enfrentamientos = df[((df['Home Team Name'] == A) & (df['Away Team Name'] == B)) | ((df['Home Team Name'] == B) & (df['Away Team Name'] == A))]
num_enfrentamientos = len(enfrentamientos)
print(f"{A} y {B} se han enfrentado {num_enfrentamientos} veces en los mundiales.")