# Tell Application

Tell adalah aplikasi analisis sentimen berbasis **Large Language Model (LLM)** yang dirancang untuk menganalisis emosi dari video yang diunggah oleh pengguna. Aplikasi ini memanfaatkan kekuatan **BERT** untuk analisis sentimen teks dan **Whisper AI** untuk ekstraksi teks dari audio video. Proyek ini menggunakan dataset emosi dari Twitter untuk melakukan fine-tuning model BERT agar dapat mengenali enam jenis sentimen emosi.

---

## Fitur Utama

1. **Analisis Sentimen Emosi**
   - Aplikasi dapat mengenali **6 jenis sentimen emosi**, seperti:
     - Joy
     - Sad
     - Angry
     - Netral
     - Fear
     - Love

2. **Ekstraksi Audio dari Video**
   - Menggunakan **Whisper AI** untuk mengekstraksi teks dari audio dalam video yang diunggah.

3. **Pengolahan Teks**
   - Teks yang diekstraksi diproses menggunakan model BERT yang telah dilatih untuk menghasilkan analisis sentimen yang akurat.

4. **Analisa Hasil**
   - Memberikan hasil analisis dalam bentuk persentase tabel.

---

## Spesifikasi Dataset

- **Sumber Dataset**: Dataset berasal dari Twitter dengan konten berbasis teks.
- **Ukuran Dataset**: 7080 baris x 2 kolom.
  - Kolom 1: Teks tweet.
  - Kolom 2: Label emosi (kategori).

---

## Teknologi yang Digunakan

1. **Model**:
   - **BERT**: Digunakan untuk analisis sentimen berbasis teks.
   - **Whisper AI**: Digunakan untuk transkripsi audio ke teks dari video yang diunggah.

2. **Bahasa Pemrograman**:
   - Python

3. **Library Utama**:
   - `transformers`: Untuk implementasi BERT.
   - `torch`: Framework machine learning.
   - `whisper`: Untuk implementasi Whisper AI.
   - `pandas`: Untuk manipulasi dataset.

---

## Cara Kerja

1. **Upload Video**: Pengguna mengunggah video melalui antarmuka aplikasi.
2. **Transkripsi Audio**: Whisper AI mengekstraksi audio dari video dan mengonversinya menjadi teks.
3. **Analisis Sentimen**:
   - Teks hasil transkripsi diproses menggunakan model BERT.
   - Hasilnya adalah klasifikasi ke salah satu dari enam jenis sentimen emosi.
4. **Output**:
   - Hasil analisis ditampilkan dalam bentuk grafik atau laporan tekstual.

---

## Cara Menjalankan Aplikasi

### 1. Persyaratan Sistem
- Python 3.8 atau lebih baru
- Library berikut harus terpasang:
  ```bash
  pip install torch transformers whisper pandas matplotlib seaborn
  ```

### 2. Langkah-langkah
1. Clone repositori ini:
   ```bash
   git clone https://github.com/WiefranVarenzo/TellMe.git
   ```
2.Karena Modelnya terlalu besar, jalankan saya Google Colabnya, kemudian download model terbaik
3. Jalankan script utama:
   ```bash
   python app.py
   ```
4. Buka aplikasi melalui browser di `http://localhost:5000` (atau port yang sesuai).

Selamat menggunakan aplikasi Tell! 🎉

