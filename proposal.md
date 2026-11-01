# PROPOSAL PROYEK AKHIR MATHQUIZ
## Program Generator dan Evaluasi Latihan Soal Matematika Berbasis Python

### 1. Latar Belakang
Matematika merupakan mata pelajaran yang membutuhkan latihan
secara rutin untuk meningkatkan pemahaman dan keterampilan
berhitung. Namun, latihan soal yang dilakukan secara manual
terkadang kurang praktis dan tidak memberikan evaluasi secara
langsung.

Oleh karena itu, dibuat program MathQuiz berbasis Python
yang dapat menghasilkan soal matematika secara acak,
memeriksa jawaban, menghitung nilai, dan memberikan
evaluasi hasil latihan secara otomatis.

### 2. Tujuan Proyek
1. Membuat program latihan soal matematika berbasis Python.
2. Menghasilkan soal matematika secara acak.
3. Memeriksa jawaban pengguna secara otomatis.
4. Menghitung nilai dan memberikan evaluasi.
5. Menyimpan riwayat hasil latihan pengguna.

### 3. Sasaran Pengguna
Siswa dan pengguna yang ingin berlatih operasi dasar
matematika secara mandiri.

### 4. Fitur Program
- Generator soal penjumlahan.
- Generator soal pengurangan.
- Generator soal perkalian.
- Generator soal pembagian.
- Pemeriksaan jawaban otomatis.
- Perhitungan nilai akhir.
- Evaluasi hasil latihan.
- Penyimpanan riwayat latihan.

### 5. Kebutuhan Program

#### A. Perangkat Lunak
- Python 3
- Visual Studio Code
- Git dan GitHub

#### B. Kebutuhan Fungsional
1. Program menampilkan menu utama.
2. Pengguna dapat memulai latihan.
3. Program menghasilkan 10 soal secara acak.
4. Pengguna memasukkan jawaban.
5. Program memeriksa jawaban.
6. Program menghitung nilai akhir.
7. Program menampilkan evaluasi.
8. Program menyimpan riwayat latihan.

#### C. Kebutuhan Nonfungsional
- Program mudah digunakan.
- Kode mudah dibaca dan dikembangkan.
- Program menangani input tidak valid.
- Data riwayat dapat disimpan.

### 6. Algoritma Program
1. Mulai.
2. Tampilkan menu utama.
3. Pengguna memilih menu latihan.
4. Masukkan nama peserta.
5. Buat 10 soal matematika secara acak.
6. Tampilkan soal satu per satu.
7. Pengguna memasukkan jawaban.
8. Periksa jawaban pengguna.
9. Hitung jumlah jawaban benar dan salah.
10. Hitung nilai akhir.
11. Tampilkan hasil evaluasi.
12. Simpan riwayat latihan.
13. Kembali ke menu utama.
14. Selesai.

### 7. Struktur Program
Pertemuan 15_Gugun Ramdani_Proyek_MathQuiz
- README.md
- proposal.md
- .gitignore
- data/
  - riwayat_latihan.txt
- src/
  - __init__.py
  - main.py
  - generator.py
  - evaluasi.py
  - utilitas.py
- tests/
  - test_case.md
  - test_program.py
- output/
  - .gitkeep

### 8. Struktur Fungsi
| File | Fungsi |
|---|---|
| main.py | Program utama dan menu |
| generator.py | Membuat soal acak |
| evaluasi.py | Memeriksa jawaban dan menghitung nilai |
| utilitas.py | Input, output, dan penyimpanan data |

### 9. Rencana Pengujian
Pengujian dilakukan untuk memastikan program
berjalan sesuai kebutuhan.

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Generator soal | Menghasilkan 10 soal |
| 2 | Jawaban benar | Status benar |
| 3 | Jawaban salah | Status salah |
| 4 | Perhitungan nilai | Nilai sesuai jumlah jawaban benar |
| 5 | Input tidak valid | Meminta input ulang |
| 6 | Data kosong | Tidak menyebabkan error |

### 10. Hasil yang Diharapkan
Program MathQuiz diharapkan dapat membantu pengguna berlatih matematika secara mandiri melalui soal acak, pemeriksaan jawaban otomatis, dan evaluasi hasil latihan.

### 11. Penutup
Proyek MathQuiz dibuat sebagai penerapan materi Algoritma dan Pemrograman menggunakan Python. Melalui proyek ini, mahasiswa diharapkan mampu menerapkan konsep algoritma, fungsi, struktur data pengolahan file, pengujian program, serta penggunaan Git dan GitHub.
