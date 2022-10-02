# Laporan Proyek Content-based Filtering - Muhammad Elfikry

## Project Overview

Teknologi pada saat ini telah berkembang dan mengalami peningkatan yang sedemikian rupa, hal ini dapat diketahui dari banyaknya kegiatan manusia yang bembutuhkan teknologi dalam penerapannya, tidak terkecuali dalam kegiatan membaca buku. Buku sudah menjadi ladang informasi bagi kalangan masyarakat. Kegiatan membaca buku juga telah menjadi hobi ataupun kebiasaan bagi sebagian orang. Banyaknya jumlah buku baru yang diterbitkan dengan berbagai macam judul menjadi suatu permasalahan baru bagi orang-orang yang memiliki ketertarikan dalam membaca buku untuk menemukan buku baru yang akan dibaca selanjutnya. Masalah tersebut dapat diatasi dengan memberikan informasi mengenai daftar buku-buku apa saja yang cocok untuk dibaca oleh pembaca berdasarkan preferensi oleh *user*(pembaca). Oleh karena itu diperlukan suatu sistem yang dapat memberikan informasi mengenai daftar buku-buku yang berkaitan dengan preferensi pembaca.

Sistem rekomendasi merupakan suatu sistem yang dapat memprediksi *rating* atau preferensi pengguna terhadap *item* tertentu. Rekomendasi ini dibuat berdasarkan perilaku pengguna di masa lalu atau perilaku pengguna lainnya. Jadi, sistem ini akan merekomendasikan sesuatu terhadap pengguna berdasarkan data perilaku atau preferensi dari waktu ke waktu. Sistem ini tidak merekomendasikan item secara spesifik. Ia merekomendasikan sejumlah item yang mungkin cocok dengan preferensi pengguna. Oleh karena itu, pada sistem rekomendasi, keluarannya berupa *“top-N” recommendation*. Artinya, mesin akan memberikan sejumlah rekomendasi dengan peringkat teratas sesuai preferensi pengguna. Model rekomendasi sangat diperlukan agar rekomendasi yang diberikan oleh sistem sesuai dengan kesukaan *user*, serta mempermudah user mengambil keputusan dalam menentukan buku apa yang akan dipilih. Salah satu metode yang dapat digunakan dalam membangun sistem rekomendasi adalah *content-based filtering. content-based filtering* adalah model yang merekomendasikan *item* yang mirip dengan *item* yang disukai pengguna di masa lalu.

## Business Understanding
### Problem Statements
Berdasarkan penjelasan pada latar belakang, maka dapat dirumuskan permasalahan sebagai berikut:
- bagaimana cara membuat sistem rekomendasi berdasarkan preferensi pengguna?
- bagaimana cara membangun model *content-based filtering*?

### Goals
- mengetahui cara membuat sistem rekomendasi berdasarkan preferensi pengguna
- mengetahui cara membangun model *content-based filtering*

### Solution statements
- Melakukan analisis *dataset* dengan cara menangani *missing values* dan mebuat korelasi pada data
- Melakukan eksplorasi data
- Membuat model yang dapat memberikan rekomendasi berdasarkan preferensi pembaca berdasarkan korelasi data dengan menggunakan *contend-based filtering*

## Data Understanding
Dataset yang digunakan pada *model machine learning* ini didapatkan dari website "kaggle.com". Untuk mendapatkan langsung dataset dapat mengunjungi *link* berikut. [Goodreads-books](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks). Dataset pada *link* tersebut memiliki format .csv dan memiliki 11123 *records* dan 12 *columns*.
### Variabel-variabel pada Goodreads-books dataset adalah sebagai berikut:
1. *bookID* = kode unik buku
2. *title* = judul buku
3. *authors* = nama pengarang buku
4. *average_rating* = penilaian rata-rata yang diberikan pengguna
5. *isbn* = kode unik standar internasional
6. *isbn13* = 13 digit kode unik standar international
7. *language_code* = bahasa yang digunakan pada buku
8. *num_pages* = jumlah halaman buku
9. *rating_count* = jumlah rating
10. *text_reviews_count* = jumlah ulasan teks pada buku
11. *publication_date* = tanggal publikasi buku
12. *publisher* = penerbit dari buku
### Exploratory data analysis
- Informasi dari data book

Tabel 1. book info

pada tabel 1 ditunjukan informasi dari data book

| #  | Column            | Non-Null Count | Dtytpe  |
|----|-------------------|----------------|---------|
| 0  | bookID            | 11123 non-null | int64   |
| 1  | title             | 11123 non-null | object  |
| 2  | authors           | 11123 non-null | object  |
| 3  | average-rating    | 11123 non-null | float64 |
| 4  | isbn              | 11123 non-null | object  |
| 5  | isbn13            | 11123 non-null | int64   |
| 6  | languages_code    | 11123 non-null | object  |
| 7  | num_pages         | 11123 non-null | int64   |
| 8  | ratings_count     | 11123 non-null | int64   |
| 9  | text_review_count | 11123 non-null | int64   |
| 10 | publication_date  | 11123 non-null | object  |
| 11 | publisher         | 11123 non-null | object  |



## Data Preparation
Tahapan yang digunakan untuk membuat model dan memberikan rekomendasi buku adalah sebagai berikut:
- Melakukan *load library* = Digunakan untuk membuat beberapa *library python* yang dibutuhkan untuk mengolah data, membangun model dan memberikan rekomendasi buku
- Melakukan *load dataset* = Digunakan untuk memuat *dataset* yang akan digunakan untuk membangun model rekomendasi
- Melakukan *univariate exploratory data analysis* = melakuakn visualisasi pada data untuk mengetahui bentuk dari data.
- Memeriksa *Missing Value* pada data = Melakukan pemeriksaan pada *dataset* apakah terdapat *missing value* pada data menggunakan fungsi *isnull()* pada *dataframe* kemudian melakukan pencetakan menggunakan fungsi *print()*. hal ini berguna untuk memudahkan model dalam melakukan proses *training*.
- Mengurutkan data = mengurutkan data berdasarkan *isbn* dari data terkecil hingga data terbesar menggunakan fungsi *sort_values*.
- Menghapus data duplikat = menghapus data duplikat berdasarkan isbn menggunkan  fungsi *drop_duplicates*

## Modeling
Pada proyek ini dalam membangun sistem rekomendasi digunakan moodel dengan teknik *Content Based Filtering*. *content-based filtering* adalah teknik yang merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu. *Content-based filtering* mempelajari *profil* minat pengguna baru berdasarkan data dari objek yang telah dinilai pengguna. Algoritma ini bekerja dengan menyarankan *item* serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi. Untuk membuat profil pengguna, dua informasi ini penting bagi sistem dengan pendekatan content-based filtering: 
- Model preferensi pengguna.
- Riwayat interaksi pengguna dengan sistem rekomendasi. 

pada tahapan pembangunanya dilakukan beberapa langkah sebagai berikut: 
- Melakukan inisialisasi *TfidfVectorizer()*
- Melakukan perhitungan *idf* pada data *authors tf.fit(data["authors"])*
- Melakukan *mapping array* dari fitur *index integer* ke fitur nama menggunakan fungsi *tf.get_feature_names()*
- Melakukan *fit* pada data kemudian ditransformasikan ke bentuk matrix menggunakan fungsi *tfidf_matrix = tf.fit_transform(data["authors"])* 
- Mengubah *vektor tf-idf* dalam bentuk matriks dengan fungsi *todense tfidf_matrix.todense()*
- Membuat *dataframe* untuk melihat *tf-idf matrix*
- Menghitung *cosine similarity* pada matrix *tf-idf*
- Membuat *dataframe* dari variabel *cosine_sim* dengan baris dan kolom berupa judul buku
- Membuat fungsi *book_recommendations* untuk mendapatkan rekomendasi.
Dari tahapan-tahapan tersebut dapat dihasilkan sistem rekomendasi yang menghasilakan beberapa keluaran yang direkomendasikan sebagai berikut:

Tabel 2. Hasil rekomendasi buku

| title                                     | authors            |
|-------------------------------------------|--------------------|
| Galapagos: A Natural History              | Michael H. Jackson |
| ER Vets: Life in an Animal emergency Room | Donna M. Jackson   |
| Wallace Stenger: His Life and Work        | Jackson J. Benson  |
| Hide(Detective D.D Warren #2)             | Lisa Gardner       |
| The Third Victim(Quincy & Rainie #2)      | Lisa Gardner       |
 
## Evaluation
Evaluasi pada proyek ini menggunkan *TF-IDF Vectorizer*.

*TF-IDF Vectorizer*

*TF-IDF Vectorizer* merupakan teknik yang akan digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap buku. Metode ini akan menghitung nilai *Term Frequency* (TF) dan *Inverse Document Frequency* (IDF). Secara sederhana, metode *TF-IDF* digunakan untuk mengetahui berapa sering suatu kata muncul di dalam dokumen. Metode ini juga terkenal efisien, mudah dan memiliki hasil yang akurat. kekurangan *TF-IDF* sejatinya berdasarkan pada *Bag of Words* (BoW), sehingga *TF-IDF* pun tidak bisa menangkap posisi teks dan semantiknya. *TF-IDF* hanya berguna sebagai fitur di level leksikal. Pada hasil evaluasi ini sistem dapat memberikan 5 keluaran hasil rekomendasi berdasarkan buku yang dibaca sebelumnya oleh pembaca.

## Conclusion
Proses analisis pada dataset menghasilkan model yang dapat memberikan rekomendasi menggunakan teknik *Content Based Filtering*. Hasil akhir dari model ini ialah menghasilkan 5 keluaran rekomendasi buku yang mirip berdasarkan buku yang sebelumnya pernah dibaca oleh pembaca yang terdiri dari judul dan nama pengarang buku. dengan model sistem rekomendasi ini diharapkan para pembaca akan dengan mudah menemukan buku baru yang cocok dan sesaui dengan minat pembaca.

## References
[1] Scikit-learn Documentation. "TfidfVectorizer".

[2] Ricci, Francesco, et al. "Recommender Systems Handbook". Springer Media.

[3] Cremonesi, Paolo. "Course: Basic Recommender Systems".

[4] Kim, Falk. "Practical Recommender Systems". 2019. Manning Publications.

[5] Kane, Frank. "Building Recommender Systems with Machine Learning and AI".
