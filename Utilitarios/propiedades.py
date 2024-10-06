import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Listas de valores posibles
distritos = ['Miraflores', 'San Isidro', 'Surco', 'La Molina', 'Barranco',
             'San Borja', 'Magdalena', 'Pueblo Libre', 'Chorrillos', 'San Miguel']
estados_inmueble = ['Nueva', 'Excelente', 'Buena', 'Regular', 'Para Remodelar']
si_no = [True, False]  # Para variables booleanas
tipo_vista = ['Parque', 'Calle', 'Mar', 'Sin Vista']
tipo_propiedad = ['Departamento', 'Casa',
                  'Duplex', 'Penthouse', 'Casa de Campo']

# Generar datos sintéticos
np.random.seed(42)  # Para reproducibilidad
num_propiedades = 10000  # Número de propiedades en el dataset

# Generación de fechas de publicación aleatorias en el rango de 2 años
fecha_base = datetime(2022, 1, 1)
fechas_pub = [fecha_base + timedelta(days=np.random.randint(0, 730))
              for _ in range(num_propiedades)]

# Generación de áreas coherentes
# Area total entre 60 y 600 m²
area_total = np.random.uniform(60, 600, num_propiedades)
porcentaje_construido = np.random.uniform(
    0.5, 1.0, num_propiedades)  # Entre 50% y 100% del area total
area_construida = area_total * porcentaje_construido

# Distribución geográfica basada en distritos
coordenadas_distritos = {
    'Miraflores': {'latitud': (-12.12, -12.08), 'longitud': (-77.05, -77.00)},
    'San Isidro': {'latitud': (-12.10, -12.08), 'longitud': (-77.05, -77.02)},
    'Surco': {'latitud': (-12.15, -12.09), 'longitud': (-77.03, -76.95)},
    'La Molina': {'latitud': (-12.10, -12.05), 'longitud': (-76.95, -76.90)},
    'Barranco': {'latitud': (-12.16, -12.13), 'longitud': (-77.03, -77.00)},
    'San Borja': {'latitud': (-12.11, -12.07), 'longitud': (-77.02, -77.00)},
    'Magdalena': {'latitud': (-12.09, -12.06), 'longitud': (-77.08, -77.05)},
    'Pueblo Libre': {'latitud': (-12.08, -12.05), 'longitud': (-77.07, -77.04)},
    'Chorrillos': {'latitud': (-12.20, -12.15), 'longitud': (-77.03, -76.95)},
    'San Miguel': {'latitud': (-12.08, -12.05), 'longitud': (-77.10, -77.05)}
}

# Generar datos
data = {
    # Antiguedad entre 0 y 40 años
    'Antiguedad': np.random.randint(0, 40, num_propiedades),
    # Entre 1 y 4 banios
    'NroBanios': np.random.randint(1, 5, num_propiedades),
    # Entre 1 y 5 dormitorios
    'Dormitorios': np.random.randint(1, 6, num_propiedades),
    # Entre 0 y 3 cocheras
    'Cocheras': np.random.randint(0, 4, num_propiedades),
    'Estado de Inmueble': np.random.choice(estados_inmueble, num_propiedades),
    'Area_construida_m2': area_construida,
    'Area_total_m2': area_total,
    'Tipo de propiedad': np.random.choice(tipo_propiedad, num_propiedades),
    'Pisos': np.random.randint(1, 3, num_propiedades),  # Entre 1 y 2 pisos
    'Vista': np.random.choice(tipo_vista, num_propiedades),
    'Fecha_pub': fechas_pub,  # Fecha de publicación
    'Distrito': [],  # Se llenará con los distritos
    'Latitud': [],  # Coordenadas geográficas
    'Longitud': [],
    # Características adicionales
    'Cuarto de servicio': np.random.choice(si_no, num_propiedades),
    'Deposito': np.random.choice(si_no, num_propiedades),
    'Terraza': np.random.choice(si_no, num_propiedades),
    'Kitchenette': np.random.choice(si_no, num_propiedades),
    'Sala de estar': np.random.choice(si_no, num_propiedades),
    'Sotano': np.random.choice(si_no, num_propiedades),
    'Patio': np.random.choice(si_no, num_propiedades),
    'Comedor diario': np.random.choice(si_no, num_propiedades),
    'Bano de servicio': np.random.choice(si_no, num_propiedades),
    'Jardin Interno': np.random.choice(si_no, num_propiedades),
    'Walking Closet': np.random.choice(si_no, num_propiedades),
    'Escritorio': np.random.choice(si_no, num_propiedades),
    'Bano independiente': np.random.choice(si_no, num_propiedades),
    'Lavanderia': np.random.choice(si_no, num_propiedades),
    'Balcon': np.random.choice(si_no, num_propiedades),
    'Bano de visitas': np.random.choice(si_no, num_propiedades),
    'Agua': np.random.choice(si_no, num_propiedades),
    'Luz': np.random.choice(si_no, num_propiedades),
    'Internet': np.random.choice(si_no, num_propiedades),
    'Sistema de seguridad': np.random.choice(si_no, num_propiedades),
    'Piscina': np.random.choice(si_no, num_propiedades),
    'Solarium': np.random.choice(si_no, num_propiedades),
    'Colegios cercanos': np.random.choice(si_no, num_propiedades),
    'Parques cercanos': np.random.choice(si_no, num_propiedades),
    'Cerca al mar': np.random.choice(si_no, num_propiedades),
    'Frente al mar': np.random.choice(si_no, num_propiedades),
    'Area de BBQ': np.random.choice(si_no, num_propiedades),
    'Gimnasio': np.random.choice(si_no, num_propiedades),
    'Sauna': np.random.choice(si_no, num_propiedades),
    'Acceso personas discapacidad': np.random.choice(si_no, num_propiedades),
    'Proximidad a transporte': np.random.choice(['Alta', 'Media', 'Baja'], num_propiedades)
}

# Asignación de distritos y coordenadas
for _ in range(num_propiedades):
    distrito = np.random.choice(distritos)
    data['Distrito'].append(distrito)
    lat_range = coordenadas_distritos[distrito]['latitud']
    lon_range = coordenadas_distritos[distrito]['longitud']
    latitud = np.random.uniform(lat_range[0], lat_range[1])
    longitud = np.random.uniform(lon_range[0], lon_range[1])
    data['Latitud'].append(latitud)
    data['Longitud'].append(longitud)

df = pd.DataFrame(data)

# Función para generar precios realistas basados en múltiples variables


def calcular_precio(row):
    # Precio base por m² de área construida en Lima (ajustable según realidad)
    precio_base_m2 = 1500

    # Ajuste de precio base por distrito
    if row['Distrito'] in ['Miraflores', 'San Isidro', 'Barranco']:
        precio_base_m2 *= 1.5  # Zonas más caras
    elif row['Distrito'] in ['Surco', 'San Borja', 'La Molina']:
        precio_base_m2 *= 1.2
    else:
        precio_base_m2 *= 1.0  # Otros distritos

    # Ajuste por tipo de propiedad
    tipo_ajuste = {
        'Departamento': 0.9,
        'Casa': 1.0,
        'Duplex': 1.1,
        'Penthouse': 1.3,
        'Casa de Campo': 1.2
    }
    precio_base_m2 *= tipo_ajuste[row['Tipo de propiedad']]

    # Precio basado en área construida con componente no lineal
    precio = precio_base_m2 * (row['Area_construida_m2'] ** 0.95)

    # Ajustes adicionales por antiguedad (efecto no lineal)
    precio *= np.exp(-row['Antiguedad'] / 50)  # Depreciación exponencial

    # Aumento por dormitorios y banios (efecto decreciente)
    precio += 10000 * np.log1p(row['Dormitorios'])
    precio += 8000 * np.log1p(row['NroBanios'])

    # Ajuste por estado del inmueble
    estado_ajuste = {
        'Nueva': 1.2,
        'Excelente': 1.1,
        'Buena': 1.0,
        'Regular': 0.85,
        'Para Remodelar': 0.7
    }
    precio *= estado_ajuste[row['Estado de Inmueble']]

    # Ajustes por características adicionales
    features_bonus = ['Cuarto de servicio', 'Deposito', 'Terraza', 'Piscina',
                      'Balcon', 'Cerca al mar', 'Frente al mar', 'Gimnasio', 'Sauna', 'Walking Closet']
    for feature in features_bonus:
        if row[feature]:
            precio += 4000  # Aumento por cada característica especial

    # Ajuste por proximidad al transporte
    if row['Proximidad a transporte'] == 'Alta':
        precio *= 1.05
    elif row['Proximidad a transporte'] == 'Baja':
        precio *= 0.95

    # Ajuste por fecha de publicación (simulando inflación o tendencia del mercado)
    dias_desde_publicacion = (datetime.now() - row['Fecha_pub']).days
    precio *= 1 + (dias_desde_publicacion / 365) * 0.02  # 2% anual

    # Introducir aleatoriedad controlada
    precio *= np.random.uniform(0.95, 1.05)  # Variabilidad del 5%

    # Evitar precios negativos
    return max(precio, 20000)  # Precio mínimo de 20,000 USD


# Calcular precios
df['Precio'] = df.apply(calcular_precio, axis=1)

df['Precio'] = df['Precio'].round(2)

# Exportar el dataframe a un archivo CSV
df.to_csv('propiedades_lima.csv', index=False)

# Mostrar las primeras filas del dataset generado
print(df.head())
