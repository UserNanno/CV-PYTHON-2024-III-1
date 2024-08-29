import random
import pandas as pd

# Función para generar la tasa de morosidad según ingresos, gastos y tipo de producto


def calcular_tasa_morosidad(ingreso, gasto, tipo_producto):
    if tipo_producto == "Hipoteca":
        # Hipotecas suelen tener menor morosidad
        return random.uniform(0.0, 0.05)
    elif gasto > ingreso * 0.8:  # Si el gasto es mayor al 80% del ingreso
        # Mayor probabilidad de morosidad
        return min(1.0, random.uniform(0.1, 0.5))
    else:
        return random.uniform(0.0, 0.1)  # Menor probabilidad de morosidad

# Función para asignar segmentos de clientes


def asignar_segmento(edad, ingreso, num_productos):
    if edad < 30 and ingreso > 5000 and num_productos > 2:
        return "Jóvenes Emprendedores"
    elif edad < 50:
        return "Familias" if ingreso < 10000 else "Emprendedores"
    elif ingreso > 15000:
        return "Inversionistas"
    else:
        return "Retirados"

# Función para generar un número de DNI único


def generar_dni_unico(dnis_existentes):
    while True:
        dni = random.randint(10000000, 99999999)
        if dni not in dnis_existentes:
            dnis_existentes.add(dni)
            return dni

# Función para generar una región aleatoria


def generar_region():
    return random.choice(["Lima", "Arequipa", "Trujillo", "Cusco", "Piura"])

# Función para generar un historial de gasto mensual (últimos 12 meses)


def generar_historial_gasto(gasto_mensual):
    return [round(gasto_mensual * random.uniform(0.8, 1.2), 2) for _ in range(12)]

# Generación del dataset


def generar_dataset(num_clientes):
    data = []
    dnis_existentes = set()

    for _ in range(num_clientes):
        dni = generar_dni_unico(dnis_existentes)
        edad = random.randint(18, 70)
        ingreso_mensual = round(random.uniform(500, 20000), 2)
        gasto_mensual = round(random.uniform(
            100, min(ingreso_mensual, 15000)), 2)
        num_productos = random.randint(1, 5)
        tipo_producto = random.choice(
            ["Tarjeta de Crédito", "Préstamo Personal", "Cuenta de Ahorros", "Inversión", "Hipoteca"])
        tasa_morosidad = calcular_tasa_morosidad(
            ingreso_mensual, gasto_mensual, tipo_producto)
        segmento = asignar_segmento(edad, ingreso_mensual, num_productos)
        region = generar_region()
        historial_gasto = generar_historial_gasto(gasto_mensual)

        data.append([dni, edad, ingreso_mensual, gasto_mensual, num_productos,
                    tipo_producto, tasa_morosidad, segmento, region, historial_gasto])

    columnas = ["DNI", "Edad", "Ingreso Mensual", "Gasto Mensual", "Número de Productos",
                "Tipo de Producto", "Tasa de Morosidad", "Segmento de Cliente", "Región", "Historial de Gasto"]
    df = pd.DataFrame(data, columns=columnas)
    return df


# Generar un dataset de 1000 clientes
dataset = generar_dataset(1000)

# Guardar el dataset en un archivo CSV
dataset.to_csv("test.csv", index=False)
print("Dataset generado y guardado en 'test.csv'")
