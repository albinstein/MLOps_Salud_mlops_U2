# Imagen base
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la app y crear carpeta de reportes
COPY app/ ./app/
RUN mkdir -p /app/reports

# Exponer el puerto usado por Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app/app_prediccion_enfermedades.py", "--server.port=8501", "--server.enableCORS=false"]
