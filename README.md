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

Dashboard ini dibuat menggunakan Metabase yang dirancang untuk menganalisis attrition (tingkat keluar masuk karyawan) dalam perusahaan, menggunakan data karyawan yang telah diklasifikasikan berdasarkan beberapa faktor penting. Dashboard tersebut menyajikan beberapa visualisasi utama seperti berikut:

- Attrition Rate

     Merupakan metrik utama yang menunjukkan persentase karyawan yang keluar dari perusahaan dalam periode tertentu. Ini adalah indikator keseluruhan kesehatan SDM di perusahaan.

- Attrition by Job Satisfaction

     Menampilkan hubungan antara tingkat kepuasan kerja karyawan (biasanya dalam skala 1–4 atau 1–5) dengan kemungkinan mereka untuk mengundurkan diri.

- Attrition by Marital Status

     Menggambarkan perbedaan tingkat attrition berdasarkan status pernikahan (lajang, menikah, dll).

- Attrition by Age

     Menganalisis kelompok usia mana yang paling rentan terhadap attrition.

- Attrition by Education Field

     Melihat sebaran attrition berdasarkan latar belakang pendidikan atau jurusan studi.

- Attrition by Department

     Visualisasi ini menunjukkan tingkat pengunduran diri karyawan berdasarkan departemen (seperti Sales, HR, R&D). Tujuannya untuk mengidentifikasi departemen mana yang memiliki attrition rate tertinggi.

- Attrition by Job Role

     Menilai tingkat pengunduran diri berdasarkan jabatan atau peran pekerjaan.

- Attrition by Total Working Years

     Memeriksa keterkaitan antara total pengalaman kerja dengan keputusan untuk keluar dari perusahaan.

- Attrition by Years at Company

     Grafik ini menunjukkan hubungan antara lama masa kerja karyawan dengan kemungkinan mereka untuk mengundurkan diri. Misalnya, karyawan dengan masa kerja 0–3 tahun mungkin memiliki risiko keluar lebih tinggi.

- Attrition by Business Travel

     Menilai bagaimana frekuensi perjalanan dinas memengaruhi tingkat attrition.

- Attrition by OverTime

     Menganalisis pengaruh jam lembur terhadap kecenderungan karyawan untuk resign.

- Attrition by WorkLifeBalance
     
     Visualisasi ini menggambarkan hubungan antara tingkat keseimbangan kehidupan dan pekerjaan dengan attrition. Semakin buruk work-life balance, biasanya risiko pengunduran diri meningkat.

- Monthly Income Distribution of Employees Who Left

     Visualisasi ini menampilkan distribusi penghasilan bulanan dari karyawan yang sudah resign. Tujuannya untuk melihat apakah ada pola tertentu (misalnya, apakah karyawan dengan gaji lebih rendah cenderung lebih sering resign?).




## Conclusion

Dari hasil visualisasi, terdapat beberapa poin penting yang dapat disimpulkan:


## Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.