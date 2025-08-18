# Usar Node.js como base
FROM node:18 

# Establecer el directorio de trabajo dentro del contenedor

WORKDIR /app

# Copiar package.json y package-lock.json antes de instalar dependencias
# se puede optimizar para la cache
COPY . .

# Instalar dependencias
RUN yarn sc-install

# Copiar el resto del código después de instalar dependencias
COPY . . 

# Exponer el puerto 5173 (por defecto en Vite)
EXPOSE 8080  

# Comando por defecto para ejecutar Vue
CMD ["npm", "run", "dev"]
