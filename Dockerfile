# Dockerfile para desplegar la app de Streamlit de predicción de enfermedades

# Imagen base
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt ./
COPY app/ ./app/

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exponer el puerto que usa Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app/app_prediccion_enfermedades.py", "--server.port=8501", "--server.enableCORS=false"]
