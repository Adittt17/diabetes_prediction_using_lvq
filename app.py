import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

# Load model LVQ
with open('model_lvq.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

weights = loaded_model['weights']
labels = loaded_model['labels']

# Fungsi prediksi berdasarkan jarak Euclidean
def predict_lvq(input_data, weights, labels):
    distances = np.sqrt(np.sum((weights - input_data) ** 2, axis=1))
    idx_min = np.argmin(distances)
    return labels[idx_min]

# Judul aplikasi
st.title("Diabetes Prediction Using LVQ")

# Input fitur dari pengguna
pregnancies = st.number_input("Pregnancies", min_value=0.0, step=1.0)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("BloodPressure", min_value=0.0)
skin_thickness = st.number_input("SkinThickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0)

# Tombol prediksi
if st.button("Start"):
    # Gabungkan input menjadi array
    input_array = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf]])

    # Normalisasi input (min-max scaler dengan range dari pelatihan jika diperlukan)
    scaler = MinMaxScaler()
    scaler.fit(weights)  # Asumsi: bobot sudah dalam skala pelatihan
    input_scaled = scaler.transform(input_array)

    # Prediksi kelas
    prediction = predict_lvq(input_scaled[0], weights, labels)

    # Tampilkan hasil
    if prediction == 1:
        st.error("Result: Positive Diabetes (1)")
    else:
        st.success("Result: Negative Diabetes (0)")
