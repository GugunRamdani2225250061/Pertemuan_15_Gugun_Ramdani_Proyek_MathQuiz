from generator import buat_soal
from evaluasi import (
    periksa_jawaban,
    hitung_nilai,
    buat_evaluasi,
    hitung_benar,
    hitung_salah
)
from utilitas import (
    input_angka,
    simpan_riwayat,
    tampilkan_hasil,
    tampilkan_riwayat
)


def mulai_latihan():
    print("\n========== MATHQUIZ ==========")

    nama = input("Masukkan nama peserta: ").strip()

    if not nama:
        print("Nama tidak boleh kosong!")
        return

    daftar_soal = buat_soal(10)

    print("\nKerjakan 10 soal berikut!\n")

    for soal in daftar_soal:
        print(f"{soal['nomor']}. {soal['soal']}")

        soal["jawaban_pengguna"] = input_angka(
            "Jawaban Anda: "
        )

    daftar_soal = periksa_jawaban(daftar_soal)

    nilai = hitung_nilai(daftar_soal)
    evaluasi = buat_evaluasi(nilai)

    benar = hitung_benar(daftar_soal)
    salah = hitung_salah(daftar_soal)

    tampilkan_hasil(daftar_soal, nilai, evaluasi)

    simpan_riwayat(nama, nilai, benar, salah)

    print("\nRiwayat latihan berhasil disimpan.")


def menu_utama():
    while True:
        print("\n================================")
        print("       MATHQUIZ")
        print(" Generator dan Evaluasi Soal")
        print("================================")
        print("1. Mulai Latihan")
        print("2. Lihat Riwayat Latihan")
        print("3. Keluar")
        print("================================")

        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            mulai_latihan()

        elif pilihan == "2":
            tampilkan_riwayat()

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan MathQuiz!")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-3.")


if __name__ == "__main__":
    menu_utama()