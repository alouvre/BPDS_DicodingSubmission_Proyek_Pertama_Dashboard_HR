# 🏢 Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

Proyek ini bertujuan untuk menyelesaikan masalah attrition (pengunduran diri karyawan) di sebuah perusahaan bernama Jaya Jaya Maju dengan pendekatan berbasis data: eksplorasi data, dashboard bisnis dengan Metabase, dan pemodelan machine learning.

[Video presentasi klik disini]("https://drive.google.com/file/d/1g2O-PaZjMTQguSHtJjHE7G8SjswFN4sZ/view?usp=sharing")

<br>

## 📁 Struktur Direktori

```
submission
├───data
     ├───data_employee_final.csv
     ├───data_employee_cleaned_dashboard.csv
     ├───data_employee.csv
├───images
     ├───alouvre-dashboard01
     ├───alouvre-dashboard02
├───models
     ├───model_perceptron.pkl
     ├───scaler.pkl
     ├───label_encoder.pkl
├───metabase.db
     ├───metabase.db.mv
├───notebook.ipynb
├───prediction.py
├───README.md
├───documentation.md
├───alouvre-video
└───requirements.txt
```

📝 Penjelasan Berkas Utama:

- `models/` - Folder berisi file model (.pkl) dan objek pendukung seperti scaler dan label encoder.
- `data/` - Berisi data mentah hingga data siap pakai untuk modeling dan dashboarding.
- `metabase/` -
- `README.md` - Ini file yang berisi gambaran umum tentang proyek, misalnya tujuan, cara pakai, atau ringkasan proyek.
- `documentation.md` - Ini dokumen yang menjelaskan detail tentang proyek, bisa lebih lengkap dari README, biasanya cara kerja, spesifikasi teknis, dan lain-lain.
- `models/model_perceptron.pkl` - Ini file model machine learning yang sudah dilatih menggunakan algoritma Perceptron.
- `models/scaler.pkl` - File yang berisi scaler, biasanya digunakan untuk preprocessing data agar fitur-fiturnya berada di skala yang sama sebelum dimasukkan ke model.
- `prediction.py` - Script/program untuk melakukan prediksi menggunakan model yang sudah dilatih.
- `data/data_employee_cleaned_dashboard.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk pembuatan dashboard.
- `data/data_employee_final.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk training model.
- `data/data_employee.csv` - Dataset asli sebelum dibersihkan atau diproses.
- `notebook.ipynb` - Jupyter Notebook berisi proses pemodelan, analisis data, training model, dll.
- `metabase/metabase.db.mv.db` - File database dari Metabase yang berisi data, pertanyaan yang sudah disimpan, dan dashboard visualisasi.
- `requirements.txt` - File yang mencantumkan semua dependensi Python yang dibutuhkan untuk menjalankan proyek.

<br>

## 📊 Persiapan Business dashboarding dengan Metabase

Dataset yang digunakan berasal dari perusahaan fiktif Jaya Jaya Maju, yang tersedia di repositori berikut:

- 🔗 [Dataset Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

### Install requirements

Pastikan semua library yang dibutuhkan telah terinstall:

```python
pip install -r requirements.txt
```

### Setup metabase

Untuk menjalankan Metabase secara lokal menggunakan Docker:

```python
docker run -d -p 3000:3000 --name metabase \
  -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
  metabase/metabase
```

Setelah container berjalan, buka browser dan akses:

🌐 http://localhost:3000/setup

Untuk mulai menggunakan dashboard Metabase dan melihat visualisasi data.

### Setup supabase

- Buat akun dan login https://supabase.com/dashboard/sign-in.
- Buat new project
- Copy URI pada database setting
- Kirim dataset menggunakan sqlalchemy

  ```python
  from sqlalchemy import create_engine

  URL = "DATABASE_URL"

  engine = create_engine(URL)
  df.to_sql('dataset', engine)
  ```

<br>

## 🧠 Machine Learning Modeling

Sebuah model klasifikasi dikembangkan untuk memprediksi apakah seorang karyawan kemungkinan akan keluar dari perusahaan. Proses pemodelan difokuskan pada mengidentifikasi pola-pola dalam data yang mengindikasikan potensi attrition. Dengan model ini, departemen HR dapat mengambil langkah preventif secara proaktif untuk mempertahankan karyawan.

### ✅ `Pendekatan yang Digunakan:`

- LazyClassifier (Baseline Model Selection)

  Digunakan untuk membandingkan berbagai algoritma klasifikasi secara cepat. Algoritma Perceptron dipilih karena menghasilkan akurasi tertinggi sebesar 0.89, menjadikannya kandidat utama untuk pelatihan dan evaluasi lanjutan.

- Perceptron Classifier (Model Utama)

  Algoritma linier yang ringan dan cepat untuk klasifikasi biner. Diterapkan sebagai model utama sebelum dan sesudah proses seleksi fitur untuk mengukur pengaruh penyederhanaan fitur terhadap kinerja model.

- Random Forest Classifier (Feature Importance)

  Digunakan untuk mengidentifikasi fitur paling berpengaruh dalam keputusan model. Fitur penting yang terdeteksi mencakup:

  ```
  Age, MonthlyIncome, DailyRate, OverTime, MonthlyRate, TotalWorkingYears, YearsAtCompany, EnvironmentSatisfaction, DistanceFromHome, HourlyRate.
  ```

- Jupyter Notebook menggunakan scikit-learn dan pandas

  Merupakan lingkungan eksplorasi data dan pengembangan model berbasis Python. pandas digunakan untuk manipulasi data, scikit-learn digunakan untuk preprocessing, pelatihan model, dan evaluasi.

- Feature Selection (Berdasarkan Skor Importance ≥ 0.04)

  Fitur dengan kontribusi tertinggi terhadap keputusan model dipilih untuk menyederhanakan model dan mengurangi noise. Hal ini juga membantu dalam memahami variabel yang paling mempengaruhi keputusan resign karyawan.

- Evaluasi Model: Accuracy, Precision, Recall, F1-score, Confusion Matrix, dan ROC-AUC

  Metrik-metrik ini memberikan penilaian menyeluruh terhadap performa model.

### 📊 `Kinerja Model:`

- 📉 Sebelum Feature Selection:

  - Accuracy = 0.86, Precision = 0.87, Recall = 0.86, F1 Score = 0.86
  - Confusion Matrix:

    ```python
    [[133, 15],
    [ 10, 21]]
    ```

    📌 Interpretasi:

    Model menunjukkan performa yang seimbang dan kuat, dengan kemampuan tinggi dalam mengklasifikasikan baik karyawan yang tetap maupun yang resign. Recall sebesar 86% untuk kelas minoritas (resign) menunjukkan bahwa model cukup baik dalam mendeteksi potensi pengunduran diri.

- 📉 Setelah Feature Selection:

  - Accuracy = 0.84, Precision = 0.81, Recall = 0.84, F1 Score = 0.80
  - Confusion Matrix:

    ```python
    [[145, 3],
    [ 26, 5]]
    ```

    📌 Interpretasi:

    Setelah dilakukan feature selection, terjadi penurunan performa model terhadap kelas minoritas (resign). Meskipun klasifikasi terhadap kelas mayoritas (tetap bekerja) meningkat, kemampuan mendeteksi karyawan yang resign menurun drastis. Hal ini terlihat dari:

    - Jumlah false negatives meningkat (26 karyawan yang resign diprediksi tidak resign).
    - Recall menurun drastis untuk kelas minoritas, sehingga banyak potensi resign tidak terdeteksi dengan baik.

- 📉 Perbandingan ROC-AUC:

  - Sebelum Feature Selection: ROC-AUC = 0.82
  - Setelah Feature Selection: ROC-AUC = 0.70

    📌 Kesimpulan:

    ROC-AUC mengalami penurunan signifikan setelah feature selection, yang menandakan bahwa kemampuan model dalam membedakan antara karyawan yang akan resign dan yang tidak menjadi lebih lemah. Oleh karena itu, pemilihan fitur perlu ditinjau ulang agar tidak mengorbankan kinerja pada kelas yang justru menjadi fokus analisis (attrition prediction).

### Langkah-Langkah Menjalankan Model

Setelah proses pelatihan (training) model selesai, model tersebut disimpan/di-export dalam bentuk file menggunakan library joblib (format penyimpanan untuk model machine learning). Untuk menggunakan model tersebut pada data karyawan baru, disediakan sebuah file Python bernama prediction.py yang bisa dijalankan untuk menghasilkan prediksi.

1. Install Required Libraries

   Sebelum menjalankan prediction.py, pastikan semua library yang dibutuhkan sudah terinstal. Jalankan perintah berikut di terminal atau command prompt:

   ```python
   pip install pandas scikit-learn joblib
   ```

   Penjelasan:

   - `pandas`: Untuk membaca dan mengelola data karyawan dalam bentuk tabel (dataframe).
   - `scikit-learn`: Library utama yang digunakan untuk membangun dan menjalankan model machine learning.
   - `joblib`: Untuk memuat (load) model yang telah disimpan sebelumnya.

2. Run the Prediction Script

   Setelah semua library siap, Anda bisa menjalankan skrip prediksi dengan mengetik:

   ```python
   python prediction.py
   ```

   Penjelasan:

   - prediction.py adalah skrip Python yang berisi logika untuk:
     - Membaca data karyawan baru.
     - Memuat model prediksi yang sudah disimpan.
     - Melakukan prediksi apakah karyawan tersebut berisiko keluar (attrition) atau tidak.
     - Menampilkan atau menyimpan hasil prediksi.
