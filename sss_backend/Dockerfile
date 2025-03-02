# Dockerfile for Backend
# Save this file as backend/Dockerfile
# ---
# Usar una imagen de Python
FROM python:3.11  

# Establecer el directorio de trabajo
WORKDIR /app  

# Copiar el archivo de dependencias
COPY requirements.txt .  

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt  

# Copiar el resto del código
COPY . .  

# Exponer el puerto 8000
EXPOSE 8000  

# Comando por defecto al ejecutar el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
