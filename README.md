# Breast Cancer Prediction App

Esta aplicación permite predecir si un tumor de mama es benigno o maligno basado en 30 características clínicas, utilizando un modelo de Machine Learning previamente entrenado.
🚀 Cómo correr el proyecto

Localmente
Clona el repositorio:
git clone git@github.com:TU_USUARIO/deploy_breast_cancer.git
cd deploy_breast_cancer
Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate # En Mac/Linux
venv\Scripts\activate # En Windows
Instala las dependencias:
pip install -r requirements.txt
Corre la aplicación:
streamlit run streamlit_app.py
Abre http://localhost:8501 en tu navegador.
Usando Docker
Construye la imagen:
docker build -t cancer-predictor .
Corre el contenedor:
docker run -p 8501:8501 cancer-predictor
Luego visita http://localhost:8501.

📥 Variables de entrada del modelo

La aplicación requiere que ingreses las siguientes 30 variables numéricas:
* radius_mean
* texture_mean
* perimeter_mean
* area_mean
* smoothness_mean
* compactness_mean
* concavity_mean
* concave points_mean
* symmetry_mean
* fractal_dimension_mean
* radius_se
* texture_se
* perimeter_se
* area_se
* smoothness_se
* compactness_se
* concavity_se
* concave points_se
* symmetry_se
* fractal_dimension_se
* radius_worst
* texture_worst
* perimeter_worst
* area_worst
* smoothness_worst
* compactness_worst
* concavity_worst
* concave points_worst
* symmetry_worst
* fractal_dimension_worst

📤 Salida del modelo

El modelo genera dos resultados:
Predicción:
🟢 B: Benigno (sin cáncer)
🔴 M: Maligno (presencia de cáncer)
Confianza:
Probabilidad de la predicción, expresada en porcentaje (%).

⚙️ Consideraciones

El modelo fue entrenado originalmente con scikit-learn versión 1.4.0.
Actualmente la aplicación puede correr en ambientes con versiones más recientes (como 1.6.1).
Esto puede generar algunos warnings al cargar el modelo, pero no afecta su funcionamiento.
No es necesario actualizar el modelo salvo que se quiera reentrenar con una nueva versión.



