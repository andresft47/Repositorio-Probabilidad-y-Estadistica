import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================

# ==========================================
# CREAR FIGURA CON 4 SUBGRÁFICAS
# ==========================================
fig = plt.figure(figsize=(12, 10))

# ==========================================
# GRÁFICA 1: UN DADO DOS VECES
# ==========================================
x = np.arange(1, 7)
y = np.arange(1, 7)
X, Y = np.meshgrid(x, y)
Z = np.full((6,6), 1/36)

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')

ax1.set_title("Dado dos veces")
ax1.set_xlabel("Primer lanzamiento")
ax1.set_ylabel("Segundo lanzamiento")
ax1.set_zlabel("Probabilidad")

# ==========================================
# GRÁFICA 2: DOS DADOS
# ==========================================
Z2 = np.full((6,6), 1/36)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')

ax2.set_title("Dos dados")
ax2.set_xlabel("Dado 1")
ax2.set_ylabel("Dado 2")
ax2.set_zlabel("Probabilidad")

# ==========================================
# GRÁFICA 3: DENSIDAD UNIFORME
# ==========================================
x_cont = np.linspace(0, 1, 50)
y_cont = np.linspace(0, 1, 50)
Xc, Yc = np.meshgrid(x_cont, y_cont)
Zc = np.ones_like(Xc)

ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.plot_surface(Xc, Yc, Zc, cmap='inferno')

ax3.set_title("Densidad uniforme")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("f(x,y)")

# ==========================================
# GRÁFICA 4: REGIÓN TRIANGULAR
# ==========================================
Xt, Yt = np.meshgrid(x_cont, y_cont)
Zt = np.where(Xt + Yt <= 1, 1, 0)

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot_surface(Xt, Yt, Zt, cmap='magma')

ax4.set_title("Región triangular x + y <= 1")
ax4.set_xlabel("X")
ax4.set_ylabel("Y")
ax4.set_zlabel("Valor")

# ==========================================
# AJUSTAR ESPACIADO Y MOSTRAR
# ==========================================
plt.tight_layout()
plt.show()