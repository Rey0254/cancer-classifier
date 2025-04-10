import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Cargar datos
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "data.csv"))

# Eliminar columnas innecesarias
df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

# Codificar etiquetas
df["diagnosis"] = LabelEncoder().fit_transform(df["diagnosis"])  # M=1, B=0

# Separar características y etiquetas
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

# División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar modelo entrenado
joblib.dump(model, os.path.join(os.path.dirname(__file__), "model.pkl"))

print("Modelo entrenado y guardado como model.pkl")