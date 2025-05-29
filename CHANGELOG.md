# Changelog

Todas las modificaciones notables a este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Agregado
- Implementación inicial de la aplicación Streamlit para predicción de enfermedades.
- Dockerfile para contenerización de la aplicación.
- Archivo `requirements.txt` con las dependencias necesarias.
- Estructura de carpetas: `app/`, `reports/`, `tests/`.
- Archivo `README.md` con la documentación del sistema.

## Cambios respecto a la propuesta inicial (Semana 1)

- Se incorporaron tecnologías de versionamiento de datos y modelos.
- Se reemplazó el enfoque básico de clasificación por uno multiclase con técnicas de few-shot learning.
- Se añadió despliegue contenerizado y monitoreo automático.


### Cambiado
- Actualización de la interfaz de usuario en Streamlit para mejorar la experiencia del usuario.
- Mejora en la estructura del código para una mejor mantenibilidad.

### Eliminado
- Archivos temporales y de prueba que no eran necesarios para el repositorio principal.

## [1.0.0] - 2025-05-28

### Agregado
- Versión inicial del sistema de predicción de enfermedades utilizando Streamlit y Docker.
- Actualizacion de la documentación básica en el `README.md`.
- Implementacion de un `CHANGELOG.md`.
