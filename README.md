# 🧠 Clasificador de Cáncer de Mama con Streamlit y Docker

Este proyecto entrena un modelo de IA para predecir si un tumor es **maligno** o **benigno** basado en características clínicas.

---

## 📦 Estructura del proyecto

```
cancer_project/
├── app/
│   ├── data/data.csv           # Dataset
│   ├── model.py                # Entrenamiento del modelo
│   ├── model.pkl               # Modelo entrenado (generado)
│   └── streamlit_app.py        # Interfaz gráfica
├── Dockerfile                  # Contenedor Docker
├── requirements.txt            # Dependencias
├── .github/workflows/train_and_build.yml  # CI/CD
└── README.md
```

---

## ▶️ ¿Cómo ejecutar localmente?

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Entrena el modelo:
```bash
python app/model.py
```

3. Inicia la app:
```bash
streamlit run app/streamlit_app.py
```

---

## 🐳 ¿Cómo ejecutar con Docker?

```bash
docker build -t cancer-model .
docker run -p 8501:8501 cancer-model
```

---

## ⚙️ CI/CD con GitHub Actions

El flujo `train_and_build.yml` entrena el modelo y construye la imagen Docker al hacer push a `main`.

---

## 📥 Variables de entrada del modelo

| Variable           | Tipo     | Descripción               |
|--------------------|----------|----------------------------|
| `radius_mean`      | float    | Radio medio del núcleo     |
| `texture_mean`     | float    | Textura media              |
| `perimeter_mean`   | float    | Perímetro medio            |
| `area_mean`        | float    | Área media                 |
| `smoothness_mean`  | float    | Suavidad media             |

---

## 📤 Salida del modelo

- `🟢 Benigno` → 0  
- `🔴 Maligno` → 1

---

## 🔐 Secretos necesarios (opcional)

Si vas a subir la imagen a DockerHub:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`