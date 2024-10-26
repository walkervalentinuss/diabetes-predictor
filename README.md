
# Diabetes Predictor using Flask and XGBoost

## Deskripsi Proyek
Proyek ini adalah **sistem prediksi risiko diabetes** yang dibangun menggunakan **Flask** sebagai backend dan **XGBoost** sebagai model machine learning. Sistem ini memungkinkan pengguna untuk memasukkan beberapa parameter kesehatan dan mendapatkan prediksi apakah seseorang berisiko terkena diabetes atau tidak.

---

## Model yang Digunakan
Model yang digunakan adalah **XGBoost Classifier**, yang merupakan salah satu algoritma machine learning berbasis **ensemble** dan terkenal dengan performa tinggi untuk prediksi.

---

## Fitur Aplikasi
- **Form input web**: User dapat mengisi data seperti glukosa, tekanan darah, insulin, dan lainnya.
- **Prediksi risiko diabetes**: Aplikasi memberikan hasil apakah pengguna berisiko terkena diabetes atau tidak.
- **API berbasis JSON**: Mendukung **curl** dan alat pengujian seperti **Postman** untuk integrasi eksternal.

---

## Cara Membuat Virtual Environment dan Menjalankan Aplikasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/diabetes-predictor.git
   cd diabetes-predictor
   ```

2. **Buat Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Aktifkan Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

   **Contoh isi `requirements.txt`:**
   ```
   Flask==2.3.2
   numpy==1.21.4
   pandas==1.3.4
   scikit-learn==0.24.2
   xgboost==1.5.0
   ```

5. **Jalankan Aplikasi Flask**:
   ```bash
   python app.py
   ```

6. **Akses Aplikasi**:
   Buka browser dan akses:  
   `http://127.0.0.1:5000`

---

## Struktur Direktori
```
diabetes-predictor/
│
├── app.py                 # Backend aplikasi Flask
├── templates/             # Folder untuk template HTML
│   └── index.html         # Tampilan frontend (form web)
├── diabetes.csv           # Dataset
├── scaler.pkl             # Scaler untuk preprocessing
├── xgb_model.pkl          # Model XGBoost terlatih
├── venv/                  # Virtual environment
├── requirements.txt       # Daftar dependensi
└── README.md              # Dokumentasi proyek
```

---

## Cara Menguji API Menggunakan Curl

Berikut adalah contoh cara menguji API menggunakan **curl**:

#### Prediksi Tidak Diabetes
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{"input": [2, 88, 70, 32, 85, 24.8, 0.5, 28]}"
```

#### Prediksi Diabetes
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{"input": [8, 190, 90, 35, 180, 38.5, 1.2, 60]}"
```

---

## Kegunaan
- **Alat evaluasi awal risiko diabetes**: Membantu pengguna memahami apakah mereka memiliki risiko terkena diabetes berdasarkan parameter kesehatan.
- **Implementasi praktis machine learning**: Memperlihatkan bagaimana **Flask** dapat digunakan untuk membangun API prediksi berbasis model machine learning.

---

## Catatan
- **Aplikasi ini bukan pengganti diagnosis medis** dan hanya memberikan hasil berdasarkan data yang dimasukkan.
- Konsultasikan dengan profesional kesehatan untuk diagnosis dan perawatan yang tepat.

---

## Lisensi
Proyek ini berlisensi di bawah **MIT License**. Silakan lihat file `LICENSE` untuk informasi lebih lanjut.
