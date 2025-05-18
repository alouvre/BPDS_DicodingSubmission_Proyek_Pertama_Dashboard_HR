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

<br>

## Business Dashboard

Dashboard ini dibangun menggunakan Metabase dan dirancang untuk menganalisis employee attrition (tingkat keluar-masuk karyawan) di perusahaan. Analisis ini dilakukan berdasarkan berbagai faktor penting yang memengaruhi keputusan karyawan untuk bertahan atau mengundurkan diri. Dashboard menyajikan sejumlah visualisasi utama sebagai berikut:

### Metrik Utama

- **Attrition Rate**

  Merupakan metrik kunci yang menunjukkan persentase karyawan yang mengundurkan diri dalam periode tertentu. Angka ini menjadi indikator umum terhadap stabilitas dan kesehatan pengelolaan sumber daya manusia di perusahaan.

### Visualisasi Berdasarkan Faktor-Faktor Demografis & Pekerjaan

| **Visualisasi**                      | **Tujuan Analisis**                                                                                                                     |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Attrition by Marital Status**      | Menggambarkan perbedaan tingkat attrition berdasarkan status pernikahan (lajang, menikah, bercerai).                                    |
| **Attrition by Age**                 | Menganalisis kelompok usia dengan tingkat attrition tertinggi dan usia-usia yang berisiko tinggi mengundurkan diri.                     |
| **Attrition by Education Field**     | Menampilkan distribusi attrition berdasarkan latar belakang pendidikan atau bidang studi.                                               |
| **Attrition by Department**          | Memvisualisasikan attrition berdasarkan departemen (Sales, R\&D, HR) untuk mengidentifikasi area dengan tingkat keluar tinggi.          |
| **Attrition by Job Role**            | Menganalisis tingkat attrition berdasarkan jabatan atau peran karyawan.                                                                 |
| **Attrition by Total Working Years** | Menggambarkan hubungan antara total pengalaman kerja dan kecenderungan mengundurkan diri.                                               |
| **Attrition by Years at Company**    | Menunjukkan korelasi masa kerja di perusahaan terhadap kemungkinan attrition, terutama pada karyawan baru (0–3 tahun).                  |
| **Attrition by Business Travel**     | Menganalisis pengaruh frekuensi perjalanan dinas terhadap keputusan keluar dari perusahaan.                                             |
| **Attrition by OverTime**            | Menilai apakah jam kerja lembur berkontribusi terhadap tingginya tingkat attrition.                                                     |
| **Attrition by Monthly Income**      | Menunjukkan distribusi pendapatan bulanan karyawan yang mengundurkan diri, untuk mengidentifikasi apakah pendapatan rendah berpengaruh. |

### Rata-Rata Indikator Kualitatif (Persepsi Karyawan)

| **Visualisasi**                       | **Tujuan Analisis**                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Average Environment Satisfaction**  | Menampilkan rata-rata kepuasan karyawan terhadap lingkungan kerja secara keseluruhan.             |
| **Average Job Satisfaction**          | Menggambarkan rata-rata tingkat kepuasan karyawan terhadap pekerjaan mereka.                      |
| **Average Job Involvement**           | Menilai rata-rata tingkat keterlibatan karyawan dalam tugas dan tanggung jawab pekerjaan.         |
| **Average Relationship Satisfaction** | Menyajikan rata-rata kepuasan karyawan terhadap hubungan interpersonal di tempat kerja.           |
| **Average Work-Life Balance**         | Menunjukkan rata-rata persepsi karyawan mengenai keseimbangan antara kehidupan kerja dan pribadi. |

<br>

## Conclusion

Dari hasil visualisasi, terdapat beberapa poin penting yang dapat disimpulkan:

<br>

## Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
