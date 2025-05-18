# 🏢 Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

Proyek ini bertujuan untuk menyelesaikan masalah attrition (pengunduran diri karyawan) di sebuah perusahaan bernama Jaya Jaya Maju dengan pendekatan berbasis data: eksplorasi data, dashboard bisnis dengan Metabase, dan pemodelan machine learning.

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
     ├───model_rf_sel.pkl
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
- `README.md` - Ini file yang berisi gambaran umum tentang proyek, misalnya tujuan, cara pakai, atau ringkasan proyek.
- `documentation.md` - Ini dokumen yang menjelaskan detail tentang proyek, bisa lebih lengkap dari README, biasanya cara kerja, spesifikasi teknis, dan lain-lain.
- `model_rf_sel.pkl` - Ini file model machine learning yang sudah dilatih menggunakan algoritma Random Forest.
- `scaler.pkl` - File yang berisi scaler, biasanya digunakan untuk preprocessing data agar fitur-fiturnya berada di skala yang sama sebelum dimasukkan ke model.
- `prediction.py` - Script/program untuk melakukan prediksi menggunakan model yang sudah dilatih tadi (rf_model.pkl).
- `data_employee_cleaned_dashboard.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk pembuatan dashboard.
- `data_employee_final.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk training model.
- `data_employee.csv` - Dataset asli sebelum dibersihkan atau diproses.
- `notebook.ipynb` - Jupyter Notebook berisi proses pemodelan, analisis data, training model, dll.
- `metabase.db.mv.db` - File database dari Metabase yang berisi data, pertanyaan yang sudah disimpan, dan dashboard visualisasi.
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

## 🧠  Machine Learning Modeling

Sebuah model klasifikasi dikembangkan untuk memprediksi apakah seorang karyawan kemungkinan akan keluar dari perusahaan. Proses pemodelan difokuskan pada mengidentifikasi pola-pola dalam data yang mengindikasikan potensi attrition. Dengan model ini, departemen HR dapat mengambil langkah preventif secara proaktif untuk mempertahankan karyawan.

### ✅ `Pendekatan yang Digunakan:`
- Random Forest Classifier
     Algoritma pohon keputusan gabungan yang andal dan kuat untuk klasifikasi.

- Jupyter Notebook menggunakan scikit-learn dan pandas

     Digunakan sebagai lingkungan pengembangan berbasis Python untuk eksplorasi data dan pelatihan model.

- Feature Importance
     
     Digunakan untuk mengidentifikasi fitur paling berpengaruh dalam keputusan model (misalnya: lembur, kepuasan kerja, usia, dll).

- Evaluasi Model: Accuracy, Precision, Recall, F1-score

     Metrik-metrik ini memberikan penilaian menyeluruh terhadap performa model, khususnya dalam menghadapi ketidakseimbangan data.

### 📊 `Kinerja Model:`
- Akurasi Keseluruhan: 85%

     📌 Artinya: Model memiliki akurasi sekitar  85 dari 100 prediksi model benar secara keseluruhan. Ini menunjukkan modelnya cukup baik dalam memprediksi attrition karyawan.

     Meskipun akurasi terlihat tinggi, hal ini sebagian besar disebabkan oleh ketidakseimbangan data—jumlah karyawan yang tetap bekerja jauh lebih banyak dibandingkan yang keluar. Hal ini menyebabkan nilai recall untuk kelas attrition (karyawan yang keluar) relatif rendah (hanya 23%), yang artinya model masih sering gagal mendeteksi karyawan yang benar-benar akan keluar.

     Oleh karena itu, peningkatan recall pada kelas attrition perlu menjadi fokus utama agar model benar-benar efektif dalam membantu HR mengambil tindakan pencegahan yang tepat.