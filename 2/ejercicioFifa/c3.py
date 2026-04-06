import pandas as pd

df = pd.read_csv('WorldCups.csv')
print('¿Quien ganó la Final del mundial de 2010? ¿Y quienes fueron los 11 jugadores titulares?')
final_2010 = df[df['Year'] == 2010].iloc[0]
ganador_2010 = final_2010['Winner']
df2 = pd.read_csv('WorldCupPlayers.csv')
jugadores_2010 = df2[df2['Team Initial'] == ganador_2010.upper()[0:3]]['Player'].tolist()
print(f"El ganador de la Final del mundial de 2010 fue {ganador_2010}.")
print(f"Los 11 jugadores titulares de {ganador_2010} en la Final de 2010 fueron: {', '.join(jugadores_2010)}.")