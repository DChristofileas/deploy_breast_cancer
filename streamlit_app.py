# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
model = joblib.load("model/logistic_regression_model_v01.pkl")



st.title("🩺 Predicción de Cáncer de Mama")
st.write("Ingrese los valores para hacer la predicción:")

# Simulamos 4 variables, modificá si tu modelo tiene otras
# Lista de variables exactas que el modelo espera
features = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean", "concave points_mean",
    "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se",
    "perimeter_se", "area_se", "smoothness_se", "compactness_se", "concavity_se",
    "concave points_se", "symmetry_se", "fractal_dimension_se", "radius_worst",
    "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave points_worst", "symmetry_worst",
    "fractal_dimension_worst"
]

# Generar los inputs dinámicamente
st.write("Ingrese los valores para hacer la predicción:")
input_data = {}
for feature in features:
    input_data[feature] = st.number_input(f"{feature}", step=0.01)

# Convertir a DataFrame de una fila
input_df = pd.DataFrame([input_data])

# Botón de predicción
if st.button("Predecir"):
    pred = model.predict(input_df)[0]
    probas = model.predict_proba(input_df)[0]

    index_map = {'B': 0, 'M': 1}
    proba = probas[index_map[pred]]

    st.subheader("Resultado:")
    if pred == 'M':
        st.error(f"🔴 Positivo para cáncer (confianza: {proba:.2%})")
    else:
        st.success(f"🟢 Negativo para cáncer (confianza: {proba:.2%})")
