# -*- coding: utf-8 -*-
"""content_based_filtering_book_recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eapkigVS4GyE5rQQzclCEoXzQjPDiCy8

## Data Loading
import library yang dibutuhkan
"""

#import library
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from google.colab import files
import pandas as pd
import numpy as np

files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d jealousleopard/goodreadsbooks

!unzip /content/goodreadsbooks.zip

"""mencetak dataset books.csv"""

books = pd.read_csv("/content/books.csv", error_bad_lines = False)

print("jumlah baris dan kolom pada data buku yang tersedia: ", books.shape)

"""## Univariate Exploratory Data Analysis"""

books.info()

"""Dataset yang digunakan memiliki 11123 records dan 12 columns:
1. bookID = kode unik buku
2. title = judul buku
3. authors = nama pengarang buku
4. average_rating = penilaian rata-rata yang diberikan pengguna
5. isbn = kode unik standar internasional
6. isbn13 = 13 digit kode unik standar international
7. language_code = bahasa yang digunakan pada buku
8. num_pages = jumlah halaman buku
9. rating_count = jumlah rating
10. text_reviews_count = jumlah ulasan teks pada buku
11. publication_date = tanggal publikasi buku
12. publisher = penerbit dari buku

menampilkan 5 data teratas pada data set
"""

books.head()

"""melakukan pencetakan jumlah dari judul buku dan judul buku"""

print("Jumlah judul buku: ", len(books["title"].unique()))
print("Judul buku: ", books["title"].unique())

"""## Data Preprocessing

membuat dataframe dengan variabel rating
"""

ratings = books[["isbn", "average_rating", "ratings_count"]]
ratings

"""menampilkan informasi pada dataframe rating"""

ratings.info()

"""melihat distribusi rating"""

ratings.describe()

"""mencetak jumlah data isbn dan jumlah data pada rating"""

print("jumlah ISBN: ", len(ratings["isbn"].unique()))
print("jumlah data rating: ", len(ratings))

"""melakukan pengelompokan dataframe berdasarkan isbn"""

books.groupby("isbn").sum()

"""membuat data baru berisikan data rating """

all_book_rate = ratings
all_book_rate

"""membuat data baru berisi nama pengarang kemudian digabungkan dengan data all_book_rate """

all_book_author = pd.merge(all_book_rate, books[["isbn", "authors"]], on="isbn", how="left")
all_book_author

"""membuat data baru berisi judul dari buku kemudian digabungkan dengan data all_book_author"""

all_book = pd.merge(all_book_author, books[["isbn", "title"]], on="isbn", how="left")
all_book

"""## Data Preparation

melakukan pemeriksaan pada data apakah terdapat missing value atau tidak
"""

# Mengecek missing value pada dataframe all_resto
all_book.isnull().sum()

"""mengurutkan data berdasarkan isbn"""

fix_book = all_book.sort_values("isbn", ascending=True)
fix_book

print("jumlah ISBN: ", len(fix_book.isbn.unique()))
print("jumlah Book-Title: ", len(fix_book["title"].unique()))

preparation = fix_book
preparation.sort_values("isbn")

"""menghapus data duplikat berdasarkan isbn"""

preparation = preparation.drop_duplicates("isbn")
preparation

"""## Model Development dengan Content Based Filtering

mencetak 5 sampel pada data
"""

data = preparation.drop(columns=["ratings_count"])
data.sample(5)

"""melakukan inisialisasi"""

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data authors
tf.fit(data["authors"]) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names()

"""melakukan fungsi fit kemudian ditrasformasikan ke dalam bentuk matrix"""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data["authors"])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""Mengubah vektor tf-idf dalam bentuk matriks"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""mebuat dataframe"""

# Membuat dataframe untuk melihat tf-idf matrix
 
pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=data.title
).sample(22, axis=1).sample(10, axis=0)

"""menghitung kesamaan pada fitur"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

"""membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa judul buku"""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa judul buku
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['title'], columns=data['title'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap judul buku
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""membuat fungsi book_recommendations"""

def book_recommendations(judul_buku, similarity_data=cosine_sim_df, items=data[['title', 'authors']], k=5):

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,judul_buku].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(judul_buku, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

data[data.title.eq("See How She Dies")]

"""mendapatkan hasil rekomendasi"""

# Mendapatkan rekomendasi judul buku yang mirip dengan See How She Dies
book_recommendations("See How She Dies")