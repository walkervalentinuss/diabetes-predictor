from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

# Inisialisasi Flask App
app = Flask(__name__)

# Memuat Model XGBoost
with open('xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Memuat Scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

print(f"Scaler type: {type(scaler)}")  # Debugging tipe scaler

# Nama fitur yang digunakan saat training dan fit scaler
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 
                 'SkinThickness', 'Insulin', 'BMI', 
                 'DiabetesPedigreeFunction', 'Age']

# Route untuk Halaman Utama
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk API Prediksi
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data input dari request JSON
        data = request.json['input']
        print(f"Received input: {data}")  # Log input untuk debugging

        # Ubah input menjadi DataFrame dengan nama kolom yang sama seperti saat fit scaler
        input_data = pd.DataFrame([data], columns=feature_names)

        # Standarisasi data input menggunakan scaler
        input_data_scaled = scaler.transform(input_data)

        # Prediksi menggunakan model
        prediction = model.predict(input_data_scaled)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        # Tangani error dan kembalikan pesan error sebagai JSON response
        print(f"Error: {e}")  # Log error untuk debugging
        return jsonify({'error': str(e)}), 400

# Menjalankan Server Flask
if __name__ == '__main__':
    app.run(debug=True)
