# Laporan Proyek Content-based Filtering - Muhammad Elfikry

## Project Overview

Teknologi pada saat ini telah berkembang dan mengalami peningkatan yang sedemikian rupa, hal ini dapat diketahui dari banyaknya kegiatan manusia yang bembutuhkan teknologi dalam penerapannya, tidak terkecuali dalam kegiatan membaca buku. Buku sudah menjadi ladang informasi bagi kalangan masyarakat. Kegiatan membaca buku juga telah menjadi hobi ataupun kebiasaan bagia sebagian orang. Banyaknya jumlah buku baru yang diterbitkan dengan berbagai macam judul menjadi suatu permasalahan baru bagi orang-orang yang memiliki ketertarikan dalam membaca buku untuk menemukan buku baru yang akan dibaca selanjutnya. Masalah tersebut dapat diatasi dengan memberikan informasi mengenai daftar buku-buku apa saja yang cocok untuk dibaca oleh pembaca berdasarkan preferensi oleh user(pembaca). Oleh karena itu diperlukan suatu sistem yang dapat memberikan informasi mengenai daftar buku-buku yang berkaitan dengan preferensi pembaca.

Sistem rekomendasi merupakan suatu sistem yang dapat memprediksi rating atau preferensi pengguna terhadap item tertentu. Rekomendasi ini dibuat berdasarkan perilaku pengguna di masa lalu atau perilaku pengguna lainnya. Jadi, sistem ini akan merekomendasikan sesuatu terhadap pengguna berdasarkan data perilaku atau preferensi dari waktu ke waktu. Sistem ini tidak merekomendasikan item secara spesifik. Ia merekomendasikan sejumlah item yang mungkin cocok dengan preferensi pengguna. Oleh karena itu, pada sistem rekomendasi, keluarannya berupa *“top-N” recommendation*. Artinya, mesin akan memberikan sejumlah rekomendasi dengan peringkat teratas sesuai preferensi pengguna. Model rekomendasi sangat diperlukan agar rekomendasi yang diberikan oleh sistem sesuai dengan kesukaan *user*, serta mempermudah user mengambil keputusan dalam menentukan buku apa yang akan dipilih. Salah satu metode yang dapat digunakan dalam membangun sistem rekomendasi adalah *content-based filtering. content-based filtering* adalah model yang merekomendasikan item yang mirip dengan *item* yang disukai pengguna di masa lalu.

## Business Understanding
### Problem Statements
Berdasarkan penjelasan pada latar belakang, maka dapat dirumuskan permasalahan sebagai berikut:
- bagaimana cara membuat sistem rekomendasi berdasarkan preferensi pengguna?
- bagaimana cara membangun model *content-based filtering*?

### Goals
- mengetahui cara membuat ssstem rekomendasi berdasarkan preferensi pengguna
- mengetahui cara membangun model *content-based filtering*

### Solution statements
- Melakukan analisis dataset dengan cara menangani missing values dan mebuat korelasi pada data
- Melakukan eksplorasi data
- Membuat model yang dapat memberikan rekomendasi berdasarkan preferensi pembaca berdasarkan korelasi data dengan menggunakan *contend-based filtering*

