# ============================================
# SISTEMA DE CONTROL DE GASTOS UNIVERSITARIOS
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import sys

# Asegurar que la salida sea UTF-8 para evitar errores de caracteres
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class ControlGastosUniversitarios:

    def __init__(self, nombre, ingreso_mensual):
        self.nombre = nombre
        self.ingreso_mensual = ingreso_mensual
        self.gastos = []

    # Registrar gasto
    def agregar_gasto(self, categoria, descripcion, valor):

        gasto = {
            "Categoria": categoria,
            "Descripcion": descripcion,
            "Valor": valor
        }

        self.gastos.append(gasto)

    # Convertir a DataFrame
    def obtener_dataframe(self):
        return pd.DataFrame(self.gastos)

    # Calcular total gastado
    def total_gastado(self):
        return sum(g["Valor"] for g in self.gastos)

    # Dinero restante
    def saldo_restante(self):
        return self.ingreso_mensual - self.total_gastado()

    # Porcentaje de gasto
    def porcentaje_gasto(self):
        if self.ingreso_mensual <= 0:
            return 0
        return (self.total_gastado() / self.ingreso_mensual) * 100

    # Nivel de riesgo financiero
    def nivel_riesgo(self):

        porcentaje = self.porcentaje_gasto()

        if porcentaje < 50:
            return "BAJO"

        elif porcentaje < 80:
            return "MEDIO"

        else:
            return "ALTO"

    # Mostrar resumen
    def mostrar_resumen(self):

        print("\n========== RESUMEN FINANCIERO ==========")
        print(f"Estudiante: {self.nombre}")
        print(f"Ingreso mensual: ${self.ingreso_mensual:,.0f}")
        print(f"Total gastado: ${self.total_gastado():,.0f}")
        print(f"Saldo restante: ${self.saldo_restante():,.0f}")
        print(f"Porcentaje gastado: {self.porcentaje_gasto():.2f}%")
        print(f"Nivel de riesgo financiero: {self.nivel_riesgo()}")

        # Alertas
        if self.nivel_riesgo() == "ALTO":
            print("\nALERTA: El estudiante está excediendo "
                  "su capacidad financiera.")

        elif self.nivel_riesgo() == "MEDIO":
            print("\nPRECAUCIÓN: El nivel de gasto es moderado.")

        else:
            print("\nBuen control financiero.")

    # Estadísticas descriptivas
    def mostrar_estadisticas(self):
        df = self.obtener_dataframe()
        if df.empty:
            return

        print("\n========== ANÁLISIS ESTADÍSTICO ==========")
        print(f"Gasto promedio: ${df['Valor'].mean():,.0f}")
        print(f"Gasto máximo:   ${df['Valor'].max():,.0f}")
        print(f"Desviación estándar: ${df['Valor'].std():,.0f}")
        print(f"Número de transacciones: {len(df)}")

    # Gráfico de gastos
    def grafico_gastos(self):

        df = self.obtener_dataframe()

        if df.empty:
            print("No hay gastos registrados.")
            return

        resumen = df.groupby("Categoria")["Valor"].sum()

        plt.figure(figsize=(8, 5))
        resumen.plot(kind="bar")

        plt.title("Distribución de Gastos")
        plt.xlabel("Categoría")
        plt.ylabel("Valor")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("distribucion_gastos.png")
        print("\nGráfico guardado como 'distribucion_gastos.png'")


# ============================================
# EJEMPLO DE USO
# ============================================

sistema = ControlGastosUniversitarios(
    "Andres Felipe",
    1200000
)

# Registrar gastos
sistema.agregar_gasto(
    "Alimentación",
    "Almuerzos universitarios",
    250000
)

sistema.agregar_gasto(
    "Transporte",
    "Pasajes",
    180000
)

sistema.agregar_gasto(
    "Entretenimiento",
    "Streaming y videojuegos",
    220000
)

sistema.agregar_gasto(
    "Educación",
    "Libros y materiales",
    150000
)

sistema.agregar_gasto(
    "Compras",
    "Ropa y accesorios",
    300000
)

# Mostrar resultados
sistema.mostrar_resumen()
sistema.mostrar_estadisticas()

# Mostrar tabla de gastos
print("\n========== DETALLE DE GASTOS ==========")
print(sistema.obtener_dataframe())

# Mostrar gráfico
sistema.grafico_gastos()