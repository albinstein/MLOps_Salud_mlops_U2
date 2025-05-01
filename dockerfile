# Dockerfile para desplegar la app de Streamlit de predicción de enfermedades

# Imagen base
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copiar archivos de la app
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install streamlit pandas

# Exponer el puerto que usa Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app_prediccion_enfermedades.py", "--server.port=8501", "--server.enableCORS=false"]
