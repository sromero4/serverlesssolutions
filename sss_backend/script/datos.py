import pandas as pd
import json

# Cargar el archivo Excel (reemplaza con tu archivo)
archivo_excel = "basedatosnapoli.xlsx"
df = pd.read_excel(archivo_excel)

# Crear una lista para los datos estructurados
datos_json = []

# Recorrer cada fila del DataFrame y construir la estructura
for index, row in df.iterrows():
    registro = {
        "id": int(index),  # Empieza en 61 como en tu caso
        "apto": str(row["APTO"]),
        "nombre_propietario": str(row["NOMBRE PROPIETARIO"]).strip() if not pd.isna(row["NOMBRE PROPIETARIO"]) else "",
        "identificacion": row["CC"] if not pd.isna(row["CC"]) else "",
        "contacto": str(row["CONTACTO"]) if not pd.isna(row["CONTACTO"]) else "",
        "propietarios": str(row["PROPIETARIOS"]).strip() if not pd.isna(row["PROPIETARIOS"]) else "",
        "cedula": row["CEDULA"] if not pd.isna(row["CEDULA"]) else "",
        "celular": str(row["CELULAR"]).strip() if not pd.isna(row["CELULAR"]) else "",
        "inquilinos": str(row["INQUILINOS"]).strip() if not pd.isna(row["INQUILINOS"]) else "",
        "placa": str(row["PLACA"]).strip() if not pd.isna(row["PLACA"]) else ""
    }
    datos_json.append(registro)

# Guardar como archivo JSON
with open("datos_convertidos.json", "w", encoding="utf-8") as f:
    json.dump(datos_json, f, ensure_ascii=False, indent=4)

print("✅ Archivo JSON creado exitosamente.")
