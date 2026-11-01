
from pathlib import Path
from datetime import datetime


ROOT_DIR = Path(__file__).resolve().parent.parent
FILE_RIWAYAT = ROOT_DIR / "data" / "riwayat_latihan.txt"


def input_angka(pesan):
    """Memastikan pengguna memasukkan bilangan bulat."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input tidak valid! Masukkan bilangan bulat.")


def simpan_riwayat(nama, nilai, benar, salah):
    """Menyimpan hasil latihan ke file TXT."""
    FILE_RIWAYAT.parent.mkdir(parents=True, exist_ok=True)

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(FILE_RIWAYAT, "a", encoding="utf-8") as file:
        file.write(
            f"{waktu} | {nama} | Nilai: {nilai:.2f} "
            f"| Benar: {benar} | Salah: {salah}\n"
        )


def tampilkan_hasil(daftar_soal, nilai, evaluasi):
    """Menampilkan hasil latihan."""
    print("\n========== HASIL LATIHAN ==========")

    for soal in daftar_soal:
        print(f"\n{soal['nomor']}. {soal['soal']}")
        print(f"Jawaban Anda : {soal['jawaban_pengguna']}")
        print(f"Kunci Jawaban: {soal['jawaban']}")
        print(f"Status       : {soal['status']}")

    print("\n===================================")
    print(f"Nilai Akhir : {nilai:.2f}")
    print(f"Evaluasi    : {evaluasi}")
    print("===================================")


def tampilkan_riwayat():
    """Menampilkan riwayat latihan."""
    print("\n========== RIWAYAT LATIHAN ==========")

    if not FILE_RIWAYAT.exists():
        print("Belum ada riwayat latihan.")
        return

    with open(FILE_RIWAYAT, "r", encoding="utf-8") as file:
        isi = file.read()

    if isi.strip():
        print(isi)
    else:
        print("Belum ada riwayat latihan.")