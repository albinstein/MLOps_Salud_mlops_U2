import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

# ---------- ESTADO INICIAL ----------
if "evaluado" not in st.session_state:
    st.session_state.evaluado = False
if "resultado" not in st.session_state:
    st.session_state.resultado = ""
if "datos_paciente" not in st.session_state:
    st.session_state.datos_paciente = {}

# ---------- RUTA Y LOG ----------
LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'reports', 'predicciones.jsonl')
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# ---------- LÓGICA DEL MODELO ----------
def modelo_simulado(data):
    temperatura = data['temperatura']
    presion_sistolica = data['presion_sistolica']
    presion_diastolica = data['presion_diastolica']
    frecuencia_cardiaca = data['frecuencia_cardiaca']
    frecuencia_respiratoria = data['frecuencia_respiratoria']
    n_sintomas = data['n_sintomas']

    if n_sintomas >= 6 and temperatura > 39 and frecuencia_respiratoria > 30:
        return "ENFERMEDAD TERMINAL"
    elif n_sintomas == 0 and temperatura < 37 and frecuencia_cardiaca < 90:
        return "NO ENFERMO"
    elif n_sintomas <= 2 and temperatura < 38:
        return "ENFERMEDAD LEVE"
    elif temperatura >= 38 or frecuencia_cardiaca >= 110 or presion_sistolica < 90:
        return "ENFERMEDAD AGUDA"
    elif n_sintomas >= 3 and presion_diastolica > 90 and frecuencia_respiratoria > 20:
        return "ENFERMEDAD CRÓNICA"
    else:
        return "ENFERMEDAD LEVE"

# ---------- FUNCIONES DE REGISTRO Y ESTADÍSTICAS ----------
def registrar_prediccion(resultado, datos):
    log = {
        "fecha": datetime.now().isoformat(),
        "prediccion": resultado,
        "datos": datos
    }
    with open(LOG_FILE, "a", encoding='utf-8') as f:
        f.write(json.dumps(log) + "\n")

def obtener_estadisticas():
    if not os.path.exists(LOG_FILE):
        return {}, [], None
    with open(LOG_FILE, "r", encoding='utf-8') as f:
        registros = [json.loads(line) for line in f]
    conteo = {}
    for r in registros:
        categoria = r["prediccion"]
        conteo[categoria] = conteo.get(categoria, 0) + 1
    ultimos_5 = registros[-5:]
    fecha_ultima = registros[-1]["fecha"] if registros else None
    return conteo, ultimos_5, fecha_ultima

# ---------- EXPORTACIONES ----------
def exportar_excel(ultimos_registros):
    df = pd.DataFrame([
        {
            "Fecha": r["fecha"],
            "Predicción": r["prediccion"],
            **r.get("datos", {})
        }
        for r in ultimos_registros
    ])
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Predicciones')
    output.seek(0)
    return output

def exportar_pdf(ultimos_registros):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Reporte de Predicciones Médicas", ln=True, align="C")
    pdf.ln(10)

    for i, r in enumerate(ultimos_registros[::-1]):
        pdf.set_font("Arial", style='B', size=11)
        pdf.cell(200, 8, f"{i+1}. {r['fecha']} - {r['prediccion']}", ln=True)
        pdf.set_font("Arial", size=10)
        datos = r.get("datos", {})
        for k, v in datos.items():
            if isinstance(v, list):
                v = ", ".join(v) if v else "Ninguno"
            pdf.cell(200, 6, f"{k.capitalize()}: {v}", ln=True)
        pdf.ln(5)

    pdf_output = pdf.output(dest='S').encode('latin1')
    return BytesIO(pdf_output)

# ---------- INTERFAZ STREAMLIT ----------
st.title("🩺 Sistema de Predicción de Enfermedades v2.15")
st.write("Ingresa los datos clínicos del paciente para evaluar su estado de salud.")

# Entradas
edad = st.number_input("Edad del paciente", min_value=0, max_value=120, value=30)
sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
temperatura = st.slider("Temperatura corporal (°C)", 35.0, 42.0, 37.0)
presion_sistolica = st.slider("Presión sistólica (mmHg)", 80, 200, 120)
presion_diastolica = st.slider("Presión diastólica (mmHg)", 50, 130, 80)
frecuencia_cardiaca = st.slider("Frecuencia cardiaca (lpm)", 40, 180, 75)
frecuencia_respiratoria = st.slider("Frecuencia respiratoria (rpm)", 10, 40, 18)
sintomas = st.multiselect("Seleccione los síntomas presentes", [
    "Fiebre", "Tos", "Dolor de cabeza", "Dificultad para respirar",
    "Fatiga", "Dolor muscular", "Náuseas", "Diarrea"
])

# ---------- LÓGICA DE EVALUACIÓN ----------
if not st.session_state.evaluado:
    if st.button("🩺 Evaluar estado de salud"):
        datos_paciente = {
            "edad": edad,
            "sexo": sexo,
            "temperatura": temperatura,
            "presion_sistolica": presion_sistolica,
            "presion_diastolica": presion_diastolica,
            "frecuencia_cardiaca": frecuencia_cardiaca,
            "frecuencia_respiratoria": frecuencia_respiratoria,
            "sintomas": sintomas,
            "n_sintomas": len(sintomas)
        }

        resultado = modelo_simulado({
            **datos_paciente,
            "sexo": 1 if sexo == "Femenino" else 0
        })

        registrar_prediccion(resultado, datos_paciente)

        st.session_state.resultado = resultado
        st.session_state.datos_paciente = datos_paciente
        st.session_state.evaluado = True
        st.rerun()

# ---------- MOSTRAR RESULTADO ----------
if st.session_state.evaluado:
    st.subheader("🧾 Resultado del análisis médico")
    st.success(f"Estado del paciente: {st.session_state.resultado}")
    st.info("✅ Evaluación completada. Puedes iniciar una nueva si lo deseas.")
    if st.button("🔄 Nueva evaluación"):
        st.session_state.clear()
        st.rerun()

# ---------- ESTADÍSTICAS Y EXPORTACIONES ----------
if st.button("📊 Ver estadísticas de predicciones"):
    conteo, ultimos_5, fecha_ultima = obtener_estadisticas()

    st.subheader("📌 Estadísticas generales")
    if conteo:
        df_conteo = pd.DataFrame(list(conteo.items()), columns=["Categoría", "Cantidad"])
        st.table(df_conteo)
    else:
        st.info("Aún no se han registrado predicciones.")

    if ultimos_5:
        st.subheader("📄 Últimas 5 predicciones")
        for idx, registro in enumerate(ultimos_5[::-1]):
            datos = registro.get("datos", {})
            with st.expander(f"🕒 {registro['fecha']} — {registro['prediccion']}"):
                st.markdown(f"""
                - **Edad**: {datos.get('edad', 'No disponible')} años  
                - **Sexo**: {datos.get('sexo', 'No disponible')}  
                - **Temperatura**: {datos.get('temperatura', 'No disponible')} °C  
                - **Presión Sistólica**: {datos.get('presion_sistolica', 'No disponible')} mmHg  
                - **Presión Diastólica**: {datos.get('presion_diastolica', 'No disponible')} mmHg  
                - **Frecuencia Cardíaca**: {datos.get('frecuencia_cardiaca', 'No disponible')} lpm  
                - **Frecuencia Respiratoria**: {datos.get('frecuencia_respiratoria', 'No disponible')} rpm  
                - **Síntomas**: {', '.join(datos.get('sintomas', [])) if datos.get('sintomas') else 'Ninguno'}
                """)

        st.markdown(f"📅 **Última predicción registrada:** `{fecha_ultima}`")

        excel_data = exportar_excel(ultimos_5)
        st.download_button(
            label="⬇️ Descargar reporte en Excel",
            data=excel_data,
            file_name="reporte_predicciones.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        pdf_data = exportar_pdf(ultimos_5)
        st.download_button(
            label="⬇️ Descargar reporte en PDF",
            data=pdf_data,
            file_name="reporte_predicciones.pdf",
            mime="application/pdf"
        )
    else:
        st.info("No hay predicciones recientes registradas.")
