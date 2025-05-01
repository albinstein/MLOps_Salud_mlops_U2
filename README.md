# Sistema de Predicción de Enfermedades - Streamlit

Este proyecto implementa una aplicación interactiva construida con Streamlit para predecir el estado de salud de un paciente a partir de síntomas y datos clínicos básicos. Las posibles salidas del modelo son:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA

## Estructura del Proyecto

```
├── app_prediccion_enfermedades.py
├── Dockerfile
├── README.md
```

## Requisitos

- Docker instalado en tu equipo

## Ejecución con Docker

1. **Clona este repositorio o guarda los archivos en una carpeta:**

```bash
git clone <URL-del-repositorio>
cd nombre-del-directorio
```

2. **Construye la imagen Docker:**

```bash
docker build -t prediccion-enfermedades .
```

3. **Ejecuta el contenedor:**

```bash
docker run -p 8501:8501 prediccion-enfermedades
```

4. **Abre el navegador:**

```
http://localhost:8501
```

## Archivo principal

- `app_prediccion_enfermedades.py`: contiene el código de la app con lógica básica de predicción basada en reglas clínicas.

## 🛠️ Notas técnicas

- La app está contenida en un entorno ligero basado en `python:3.10-slim`.
- Usa solo `streamlit`, `pandas` y `numpy` como dependencias.

---

Desarrollado por Albin Rivera – 2025

