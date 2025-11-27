import pandas as pd

# 1. Lectura y carga (Reemplaza las líneas 12-28 de tu código)
# Pandas maneja automáticamente los encabezados y tipos de datos.
df = pd.read_csv('car_fleet.csv')

# (Opcional) Si quieres asegurar que los vacíos sean 0 como en tu plantilla original:
df = df.fillna(0)

# 2. Imprimir nombres de columnas (Reemplaza línea 16)
print(f'Column names are: {", ".join(df.columns)}')

# 3. Convertir a lista de diccionarios (Reemplaza tu bucle y copy.deepcopy)
# Esto crea exactamente la estructura de 'myInventoryList'
myInventoryList = df.to_dict('records')

print(f'Processed {len(df) + 1} lines.') # +1 para contar el header como en tu script

# 4. Tu bucle final de impresión (Líneas 30-33)
# Puedes mantenerlo igual, ya que 'myInventoryList' tiene el mismo formato
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")