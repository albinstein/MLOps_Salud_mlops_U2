# Pipeline MLOps para Predicción de Enfermedades – v1.0.0

## Caso de Uso
### Contexto
Este sistema apoya a profesionales de la salud mediante la predicción del estado clínico de un paciente usando datos clínicos estructurados y síntomas. Integra condiciones comunes y enfermedades huérfanas. El modelo se despliega en una interfaz **Streamlit** contenerizada con **Docker**.

### Definición del Problema

#### Entrenamiento del Modelo
El modelo realiza clasificación multiclase en cinco estados:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
- ENFERMEDAD TERMINAL

Desafíos clave: desbalance de clases, interpretabilidad y escasez de datos.

---

### Parte 1: Diseño del Pipeline MLOps

#### Diagrama del Pipeline Propuesto

![Pipeline MLOps de Predicción de Enfermedades](./imgs/pipeline-mlops.png)

---

#### Ingesta de Datos
- Historias clínicas electrónicas (EHR)
- Formularios de triaje
- Bases públicas (MIMIC, Orphanet)
- Automatización con **Airflow** / **Dagster**
- Versionado con **DVC** o **LakeFS**

---

#### Procesamiento y Calidad del Dato
- Imputación de datos faltantes
- Normalización y codificación
- Aumento sintético (SMOTE, Focal Loss)

---

#### Entrenamiento del Modelo
Modelos sugeridos:
- **XGBoost**, **LightGBM**
- **MLP**, **TabTransformer**

Validación cruzada estratificada, enfoque few-shot/meta-learning para enfermedades raras.

---

#### Registro y Empaquetado
- Formatos: `.pkl`, `.joblib`, `.onnx`
- Contenerización: **Docker**
- Registro: **MLflow**, **Vertex AI**

---

#### Despliegue
- API REST con **FastAPI**
- Interfaz de usuario con **Streamlit**
- Escenarios: local o Kubernetes

---

#### Monitoreo y Reentrenamiento
- Herramientas: **Evidently AI**, **Grafana**, **Prometheus**
- Retraining programado y supervisado
- CI/CD con **GitHub Actions**, **Jenkins**, **GitLab CI**

---

### Parte 2: Caso Clínico

Un paciente masculino de 30 años con:
- Temperatura: 39.7 °C
- PA: 120/80 mmHg
- FC: 75 lpm
- FR: 18 rpm
- Síntomas: náuseas y fatiga

El sistema evalúa esta información y predice el estado clínico.

---

### Parte 3: Guía de Ejecución

#### Requisitos
- Docker instalado
- Opcional: Git

#### Pasos para ejecutar

```bash
git clone https://github.com/albinstein/MLOps_Salud_mlops_U2.git
cd MLOps_Salud_mlops_U2
docker build -t prediccion-enfermedades .
docker run -p 8501:8501 prediccion-enfermedades
```

Abre tu navegador en: [http://localhost:8501](http://localhost:8501)

---

### Estructura del Proyecto

```
MLOps_Salud_mlops_U2/
├── app/                       # Código Streamlit
│   └── app_prediccion_enfermedades.py
├── reports/                   # Reportes
├── Dockerfile                 # Imagen contenedor
├── requirements.txt           # Dependencias
├── .gitignore
├── README.md
```

---

### Repositorio

Repositorio Git principal:  
[https://github.com/albinstein/MLOps_Salud.git](https://github.com/albinstein/MLOps_Salud.git)

---


---

## Historial de Cambios

Consulta el [CHANGELOG.md](./CHANGELOG.md) para más detalles sobre las versiones y actualizaciones del proyecto.


Desarrollado por Albin Rivera – 2025