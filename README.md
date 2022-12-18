# Tugas Besar Pengolahan Bahasa Alami - Kelompok 8

## Anggota Kelompok
- Aprilia Purwanto	    119140003
- Nurul Aulia L.	    119140008
- Edinia Rosa F.	    119140018
- Romaita Maria S.	    119140039
- Husliana Pratiwi	    119140042
- Istighfariza Aprini	119140059
- Putri Dwisastika L.	119140068
- Nesa Oktavia		    119140091
- Ihza Fajrur R.H.	    119140130

## Instalasi GUI
Untuk menjalankan GUI berbasis web application, pengguna perlu untuk mengunduh beberapa dependency terlebih dahulu. Cara mengunduh dependency yang dibutuhkan adalah dengan cara mengunduh semua dependency berikut dengan menggunakan command "pip install" pada Python
- flask
- pandas
- matplotlib
- seaborn
- nltk
- scikit-learn
- spacy
- Counter

Detail lebih lanjut dapat dilihat pada file *requirements.txt*

## Deskripsi Penggunaan GUI
Pertama, jalankan file *app.py*. Selanjutnya, pengguna memasukkan masing-masing 1 kalimat ke dalam 2 inputan teks yang tersedia. Program akan mengolah inputan dalam 3 tahapan yaitu preprocessing, TF-IDF, dan Cosine Similarity. Kemiripan kedua dokumen ditentukan dari besaran cosine similarity tersebut. Semakin besar nilai cosine similarity, maka indikasi plagiarisme semakin besar.

## Metode
- Input Data dari dataset
- Preprocessing (Case folding, Tokenizing, Stopword Removal, Stemming)
- TF-IDF-DF
- Normalisasi Min-MAx
- Evaluasi (MAPE, MAE)
## Dataset
Data yang digunakan untuk training model ada pada file *SICK_train.txt*

## Hasil Evaluasi Sistem
Evaluasi sistem terdapat dalam file *model.ipynb*. Evaluasi sistem dilakukan menggunakan metrik MAE dan MAPE.
> MAE : 0.10485853726129357
> MAPE : 0.1078544954687591