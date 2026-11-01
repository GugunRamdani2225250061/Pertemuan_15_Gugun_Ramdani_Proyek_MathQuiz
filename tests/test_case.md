
# TEST CASE MATHQUIZ

## Tujuan Pengujian
Memastikan seluruh fungsi utama MathQuiz berjalan
sesuai dengan rancangan program.

## Tabel Pengujian

| ID | Fitur | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Generator soal | Jumlah 10 | Menghasilkan 10 soal | 10 soal dihasilkan | PASS |
| TC02 | Penjumlahan | 20 + 10 | 30 | 30 | PASS |
| TC03 | Pemeriksaan jawaban | Jawaban 25, kunci 25 | Benar | Benar | PASS |
| TC04 | Perhitungan nilai | 8 benar dari 10 | 80 | 80 | PASS |
| TC05 | Input tidak valid | abc | Meminta input ulang | Meminta input ulang | PASS |
| TC06 | Data kosong | List kosong | Nilai 0 | Nilai 0 | PASS |
| TC07 | Evaluasi nilai | Nilai 90 | Sangat Baik | Sangat Baik | PASS |
| TC08 | Penyimpanan riwayat | Data peserta | Data tersimpan | Data tersimpan | PASS |

## Kesimpulan
Berdasarkan pengujian, fitur utama MathQuiz dapat
berjalan sesuai dengan hasil yang diharapkan.
Pengujian dilakukan terhadap generator soal,
pemeriksaan jawaban, perhitungan nilai, validasi
input, evaluasi, dan penyimpanan riwayat.