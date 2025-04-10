import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Cargar modelo
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Clasificador de Cáncer de Mama", layout="centered")
st.title("🧠 Clasificador de Cáncer de Mama")
st.write("Este modelo predice si un tumor es maligno o benigno basado en características clínicas.")

# Entradas del usuario
with st.form("prediction_form"):
    st.subheader("📋 Ingresa los valores de las características:")
    radius_mean = st.number_input("radio medio", min_value=0.0)
    texture_mean = st.number_input("textura media", min_value=0.0)
    perimeter_mean = st.number_input("perímetro medio", min_value=0.0)
    area_mean = st.number_input("área media", min_value=0.0)
    smoothness_mean = st.number_input("suavidad media", min_value=0.0)

    submitted = st.form_submit_button("Predecir")

    if submitted:
        input_data = pd.DataFrame([[
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean
        ]], columns=[
            "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean"
        ])

        prediction = model.predict(input_data)[0]
        resultado = "🔴 Maligno" if prediction == 1 else "🟢 Benigno"
        st.subheader(f"Resultado de la predicción: {resultado}")