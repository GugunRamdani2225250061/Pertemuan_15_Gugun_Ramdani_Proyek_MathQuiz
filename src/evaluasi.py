
def periksa_jawaban(daftar_soal):
    """Memeriksa jawaban pengguna."""
    for soal in daftar_soal:
        if soal["jawaban_pengguna"] == soal["jawaban"]:
            soal["status"] = "Benar"
        else:
            soal["status"] = "Salah"

    return daftar_soal


def hitung_nilai(daftar_soal):
    """Menghitung nilai akhir pengguna."""
    if not daftar_soal:
        return 0

    benar = sum(
        1 for soal in daftar_soal
        if soal["status"] == "Benar"
    )

    return (benar / len(daftar_soal)) * 100


def buat_evaluasi(nilai):
    """Memberikan evaluasi berdasarkan nilai."""
    if nilai >= 90:
        return "Sangat Baik"
    elif nilai >= 80:
        return "Baik"
    elif nilai >= 70:
        return "Cukup"
    elif nilai >= 60:
        return "Perlu Berlatih"
    else:
        return "Perlu Belajar Lebih Giat"


def hitung_benar(daftar_soal):
    return sum(
        1 for soal in daftar_soal
        if soal["status"] == "Benar"
    )


def hitung_salah(daftar_soal):
    return len(daftar_soal) - hitung_benar(daftar_soal)