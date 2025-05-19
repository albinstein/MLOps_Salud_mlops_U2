from app.app_prediccion_enfermedades import modelo_simulado

def test_prediccion_terminal():
    datos = {
        'temperatura': 40.5,
        'presion_sistolica': 85,
        'presion_diastolica': 100,
        'frecuencia_cardiaca': 120,
        'frecuencia_respiratoria': 35,
        'n_sintomas': 7
    }
    assert modelo_simulado(datos) == "ENFERMEDAD TERMINAL"

def test_prediccion_leve():
    datos = {
        'temperatura': 37.2,
        'presion_sistolica': 120,
        'presion_diastolica': 80,
        'frecuencia_cardiaca': 85,
        'frecuencia_respiratoria': 18,
        'n_sintomas': 1
    }
    assert modelo_simulado(datos) == "ENFERMEDAD LEVE"
