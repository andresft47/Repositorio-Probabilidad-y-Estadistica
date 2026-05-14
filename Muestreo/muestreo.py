import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Cargar población desde el archivo CSV
data = pd.read_csv('poblacion_videojuegos.csv')
N = len(data)

# Parámetros
n = 500
k = N // n

# Inicio aleatorio (fijado en 8 para coincidir con los resultados previos)
inicio = 8

# Muestreo sistemático
indices = np.arange(inicio, N, k)
muestra = data.iloc[indices]

# Resultados
print(muestra.head())
print(muestra.describe().round(2))

# Comparación
print("Promedio gasto población:", round(data['Gasto_USD'].mean(), 2))
print("Promedio gasto muestra:", round(muestra['Gasto_USD'].mean(), 2))

# Gráfica
plt.figure()
plt.hist(data['Gasto_USD'], alpha=0.5, label='Población')
plt.hist(muestra['Gasto_USD'], alpha=0.5, label='Muestra')
plt.legend()
plt.title("Comparación de gasto")
plt.show()

plt.figure()
muestra['Pais'].value_counts().plot(kind='bar')
plt.title("Jugadores por país (muestra)")
plt.show()