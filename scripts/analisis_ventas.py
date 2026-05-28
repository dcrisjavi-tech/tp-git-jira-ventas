import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# PROYECTO:
# ANALISIS DE VENTAS DE UNA EMPRESA
#
# Integrantes:
# - Hugo
# - Paco
# - Luis
# =====================================

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# =====================================
# CREAR COLUMNA DE VENTAS
# =====================================

df["Ventas"] = df["Cantidad"] * df["Precio"]

# =====================================
# INDICADORES PRINCIPALES
# =====================================

print("VENTAS TOTALES:")
print(df["Ventas"].sum())

print("\nPROMEDIO DE VENTAS:")
print(df["Ventas"].mean())

# =====================================
# PRODUCTO MAS VENDIDO
# =====================================

producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()

print("\nPRODUCTO MAS VENDIDO:")
print(producto_mas_vendido)

# =====================================
# ANALISIS DE VENTAS POR MES
# =====================================

# Convertir columna Fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Agrupar ventas por mes
ventas_mes = df.groupby(df["Fecha"].dt.month)["Ventas"].sum()

print("\nVENTAS POR MES:")

for mes, venta in ventas_mes.items():
    print(f"Mes {mes}: {venta}")

# =====================================
# GUARDAR RESULTADOS EN TXT
# =====================================

with open("resultados/resumen.txt", "w") as f:

    f.write("REPORTE DE VENTAS\n")
    f.write("========================\n\n")

    f.write(f"Ventas totales: {df['Ventas'].sum()}\n")
    f.write(f"Promedio de ventas: {df['Ventas'].mean()}\n")
    f.write(f"Producto mas vendido: {producto_mas_vendido}\n\n")

    f.write("Ventas por mes:\n")

    for mes, venta in ventas_mes.items():
        f.write(f"Mes {mes}: {venta}\n")

# =====================================
# GENERAR GRAFICO
# =====================================

ventas_mes.plot(kind="bar")

plt.title("Evolucion de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas Totales")

# Guardar grafico
plt.savefig("resultados/grafico_ventas.png")

# Mostrar grafico
plt.show()