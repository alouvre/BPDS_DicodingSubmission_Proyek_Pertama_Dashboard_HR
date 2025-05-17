# Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan lebih dari 1.000 karyawan yang tersebar di seluruh Indonesia. Seiring dengan berkembangnya skala bisnis dan meningkatnya kompleksitas operasional, tantangan dalam pengelolaan sumber daya manusia pun menjadi semakin signifikan.

Salah satu permasalahan utama yang dihadapi perusahaan saat ini adalah tingginya tingkat employee attrition atau pengunduran diri karyawan, yang tercatat telah melampaui angka 10%. Angka ini cukup mengkhawatirkan karena attrition rate yang tinggi dapat menjadi indikator adanya permasalahan mendasar, seperti rendahnya kepuasan kerja, kurangnya kejelasan pengembangan karier, ketidaksesuaian kompensasi, atau ketidakseimbangan antara pekerjaan dan kehidupan pribadi.

Sebagai langkah strategis, departemen Human Resources (HR) membutuhkan alat bantu analisis berupa dashboard interaktif berbasis data. Dashboard ini diharapkan mampu menyajikan visualisasi menyeluruh terhadap berbagai faktor yang berkontribusi terhadap attrition, sehingga memudahkan proses pemantauan kondisi SDM secara real-time dan mendukung pengambilan keputusan yang cepat dan tepat. Selain itu, perusahaan juga membutuhkan dukungan model machine learning untuk memprediksi karyawan yang berpotensi mengundurkan diri. Dengan demikian, tindakan preventif dapat dilakukan lebih awal untuk mempertahankan talenta terbaik dan mengurangi tingkat attrition secara berkelanjutan.

### Permasalahan Bisnis

Bagaimana Jaya Jaya Maju dapat menurunkan tingkat attrition karyawan yang tinggi guna meningkatkan produktivitas, efisiensi operasional, serta memastikan stabilitas bisnis dalam jangka panjang?

Pertanyaan utama ini dapat dijabarkan ke dalam beberapa sub-masalah berikut:

- Apa saja faktor utama yang berkontribusi terhadap tingginya tingkat attrition di Jaya Jaya Maju?
- Sejauh mana kepuasan kerja, keseimbangan kehidupan dan pekerjaan (work-life balance), peluang pengembangan karier, serta budaya organisasi memengaruhi keputusan karyawan untuk tetap bertahan atau mengundurkan diri?
- Strategi apa yang dapat diterapkan oleh manajemen untuk meningkatkan retensi dan loyalitas karyawan secara berkelanjutan?
- Bagaimana penerapan model machine learning dapat membantu dalam memprediksi risiko pengunduran diri karyawan secara proaktif?

### Cakupan Proyek

Untuk menjawab permasalahan di atas, proyek ini memiliki dua fokus utama:

- Pembuatan Business Dashboard

  Dashboard ini dirancang untuk membantu tim HR dalam memantau berbagai faktor yang memengaruhi attrition berdasarkan data historis. Visualisasi interaktif mencakup metrik-metrik penting seperti distribusi usia, status pernikahan, kebiasaan lembur, tingkat kepuasan kerja, serta distribusi berdasarkan departemen dan jabatan.

- Pengembangan Model Machine Learning

  Proyek ini juga mencakup pengembangan model machine learning untuk memprediksi kemungkinan seorang karyawan akan mengalami attrition. Model ini diintegrasikan ke dalam antarmuka interaktif berbasis Streamlit, di mana pengguna dapat memasukkan data karyawan secara manual dan langsung memperoleh hasil prediksi. Hal ini memungkinkan tim HR untuk melakukan identifikasi dini terhadap karyawan berisiko tinggi dan merancang strategi retensi secara lebih tepat sasaran.

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
├───<username_dicoding>-video
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

## Persiapan

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

## Business Dashboard

Dashboard ini dibangun menggunakan Metabase dan dirancang untuk menganalisis employee attrition (tingkat keluar-masuk karyawan) di perusahaan. Analisis ini dilakukan berdasarkan berbagai faktor penting yang memengaruhi keputusan karyawan untuk bertahan atau mengundurkan diri. Dashboard menyajikan sejumlah visualisasi utama sebagai berikut:

### Metrik Utama

- **Attrition Rate**

     Merupakan metrik kunci yang menunjukkan persentase karyawan yang mengundurkan diri dalam periode tertentu. Angka ini menjadi indikator umum terhadap stabilitas dan kesehatan pengelolaan sumber daya manusia di perusahaan.

### Visualisasi Berdasarkan Faktor-Faktor Demografis & Pekerjaan

- Attrition by Marital Status

     Menggambarkan perbedaan tingkat attrition berdasarkan status pernikahan, seperti lajang, menikah, atau bercerai.

- Attrition by Age

     Menganalisis kelompok usia mana yang memiliki tingkat pengunduran diri paling tinggi, serta pola usia yang berisiko tinggi terhadap attrition.

- Attrition by Education Field

     Menampilkan distribusi attrition berdasarkan latar belakang pendidikan atau bidang studi karyawan.

- Attrition by Department

     Memvisualisasikan tingkat pengunduran diri berdasarkan departemen (misalnya Sales, R&D, HR), sehingga dapat diidentifikasi area mana yang memerlukan perhatian lebih dalam hal retensi karyawan.

- Attrition by Job Role

     Menganalisis tingkat attrition berdasarkan peran atau jabatan karyawan dalam organisasi.

- Attrition by Total Working Years

     Menggambarkan hubungan antara total pengalaman kerja (di seluruh karier, bukan hanya di perusahaan ini) dan kecenderungan untuk mengundurkan diri.

- Attrition by Years at Company

     Menunjukkan seberapa lama masa kerja seorang karyawan di perusahaan berkorelasi dengan kemungkinan mereka mengundurkan diri. Umumnya, karyawan dengan masa kerja 0–3 tahun lebih berisiko mengalami attrition.

- Attrition by Business Travel

     Menganalisis pengaruh frekuensi perjalanan dinas terhadap keputusan karyawan untuk bertahan atau mengundurkan diri.

- Attrition by OverTime

     Menilai dampak jam kerja lembur terhadap kecenderungan karyawan mengalami attrition.

- Attrition by Monthly Income

     Visualisasi ini menunjukkan sebaran penghasilan bulanan dari karyawan yang sudah mengundurkan diri. Hal ini bertujuan untuk mengidentifikasi apakah terdapat pola tertentu, seperti kemungkinan karyawan dengan pendapatan lebih rendah lebih rentan terhadap attrition.

### Rata-Rata Indikator Kualitatif (Persepsi Karyawan)

- Average Environment Satisfaction

     Menampilkan rata-rata kepuasan karyawan terhadap lingkungan kerja secara keseluruhan.

- Average Job Satisfaction

     Menggambarkan rata-rata tingkat kepuasan terhadap pekerjaan masing-masing.

- Average Job Involvement

     Menilai rata-rata tingkat keterlibatan karyawan dalam pekerjaannya.

- Average Relationship Satisfaction

     Menyajikan rata-rata kepuasan terhadap hubungan interpersonal di lingkungan kerja.

- Average Work-Life Balance

     Menunjukkan rata-rata persepsi karyawan terhadap keseimbangan antara pekerjaan dan kehidupan pribadi.

## Conclusion

Dari hasil visualisasi, terdapat beberapa poin penting yang dapat disimpulkan:

## Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
