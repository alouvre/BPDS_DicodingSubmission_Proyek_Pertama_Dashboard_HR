# Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

Proyek ini bertujuan untuk menyelesaikan masalah attrition (pengunduran diri karyawan) di sebuah perusahaan bernama Jaya Jaya Maju.

## Struktur Direktori

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

Penjelasan:
- `README.md` - Ini biasanya file yang berisi gambaran umum tentang proyek, misalnya tujuan, cara pakai, atau ringkasan proyek.
- `documentation.md` - Ini dokumen yang menjelaskan detail tentang proyek, bisa lebih lengkap dari README, biasanya cara kerja, spesifikasi teknis, dan lain-lain.
- `model_rf_sel.pkl` - Ini file model machine learning yang sudah dilatih menggunakan algoritma Random Forest.
- `scaler.pkl` - File yang berisi scaler, biasanya digunakan untuk preprocessing data agar fitur-fiturnya berada di skala yang sama sebelum dimasukkan ke model.
- `prediction.py` - Script/program untuk melakukan prediksi menggunakan model yang sudah dilatih tadi (rf_model.pkl).
- `data_employee_cleaned_dashboard.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk pembuatan dashboard.
- `data_employee_final.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk training model.
- `data_employee.csv` - Dataset asli sebelum dibersihkan atau diproses.
- `notebook.ipynb` - Jupyter Notebook berisi proses pemodelan, analisis data, training model, dll.
- `metabase.db.mv.db` - File database dari Metabase yang berisi data, pertanyaan yang sudah disimpan, dan dashboard visualisasi.

## Persiapan Business dashboarding dengan Metabase

Sumber data yang digunakan merupakan dataset [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

### Install requirements

```python
pip install -r requirements.txt
```

### Setup metabase

Untuk melihat dashboard secara lokal:

```python
docker run -d -p 3000:3000 --name metabase \
  -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
  metabase/metabase
```

Lalu, buka browser dan navigasikan http://localhost:3000/setup untuk mengakses dashboard Metabase..

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

## Machine Learning Modeling
