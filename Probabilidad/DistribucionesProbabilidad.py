import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# ==========================================
# CREAR FIGURA CON 3 SUBGRÁFICAS
# ==========================================
fig = plt.figure(figsize=(18, 5))

# =========================
# 1. DISTRIBUCIÓN BINOMIAL
# =========================
n = 5
p = 1/6

x_binom = np.arange(0, n+1)
y_binom = binom.pmf(x_binom, n, p)

ax1 = fig.add_subplot(1, 3, 1)
ax1.bar(x_binom, y_binom, color='skyblue', edgecolor='black')
ax1.set_title("Distribución Binomial (n=5, p=1/6)")
ax1.set_xlabel("Número de éxitos")
ax1.set_ylabel("Probabilidad")

# =========================
# 2. DISTRIBUCIÓN POISSON
# =========================
lam = 1

x_poisson = np.arange(0, 10)
y_poisson = poisson.pmf(x_poisson, lam)

ax2 = fig.add_subplot(1, 3, 2)
ax2.bar(x_poisson, y_poisson, color='lightgreen', edgecolor='black')
ax2.set_title("Distribución de Poisson (λ=1)")
ax2.set_xlabel("Número de eventos")
ax2.set_ylabel("Probabilidad")

# =========================
# 3. DISTRIBUCIÓN NORMAL
# =========================
x_normal = np.linspace(-4, 4, 1000)
y_normal = norm.pdf(x_normal, 0, 1)

ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(x_normal, y_normal, color='salmon', linewidth=2)

# sombrear área ejemplo a)
k = 0.52
x_fill = np.linspace(k, 4, 500)
y_fill = norm.pdf(x_fill)
ax3.fill_between(x_fill, y_fill, color='salmon', alpha=0.3)

ax3.set_title("Distribución Normal Estándar")
ax3.set_xlabel("Z")
ax3.set_ylabel("Densidad")

# =========================
# MOSTRAR TODAS
# =========================
plt.tight_layout()
plt.show()

print("\nVisualización finalizada.")