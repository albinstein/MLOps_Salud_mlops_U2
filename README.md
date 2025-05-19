# Sistema de Predicción de Enfermedades - Streamlit + Docker

Este proyecto implementa una aplicación interactiva construida con **Streamlit** para predecir el estado de salud de un paciente a partir de síntomas y datos clínicos básicos. Las posibles salidas del modelo son:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA

## Estructura del Proyecto

```
MLOps_Salud_mlops_U2/
├── app/
│   └── app_prediccion_enfermedades.py # Código principal de la app Streamlit
├── reports/                           # Generacion de reportes
├── Dockerfile                         # Imagen para contenerizar la app
├── requirements.txt
├── .gitignore                         # Exclusión de archivos innecesarios en Git
├── README.md                          # Documentación del sistema
```

## Requisitos

- Tener **Docker** instalado (Windows, Linux o macOS).
- Tener acceso a línea de comandos (CMD, PowerShell, Terminal).
- Opcional: Git para clonar el repositorio.

## Ejecución con Docker

1. **Clona este repositorio o guarda los archivos en una carpeta:**

```bash
git clone https://github.com/albinstein/MLOps_Salud_mlops_U2.git
cd MLOps_Salud_mlops_U2
```

O si tienes los archivos sueltos, colócalos todos en una misma carpeta.

### 2. Verifica que tengas los siguientes archivos:

- `app_prediccion_enfermedades.py`
- `Dockerfile` (con D mayúscula)
- `.gitignore`
- `README.md`

---

### 3. Construir la imagen Docker

```bash
docker build -t prediccion-enfermedades .
```

---

### 4. Ejecutar el contenedor

```bash
docker run -p 8501:8501 prediccion-enfermedades
```

Esto levantará el servidor Streamlit en el puerto 8501.

---

### 5. Abrir la aplicación en el navegador

```
http://localhost:8501
```

---

## ¿Qué hace esta aplicación?

Recibe:
- Edad, sexo, temperatura, presión arterial, frecuencia cardiaca y síntomas.

Devuelve:
- Un estado clínico estimado basado en reglas médicas programadas o un modelo predictivo (próximamente integrable).

---

## Notas técnicas

- La app está contenida en un entorno ligero basado en `python:3.10-slim`.
- Usa solo `streamlit`, `pandas` y `numpy` como dependencias.

---

Desarrollado por Albin Rivera – 2025








