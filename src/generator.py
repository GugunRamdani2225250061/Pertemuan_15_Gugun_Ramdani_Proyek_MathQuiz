import random


def buat_soal(jumlah=10):
    """Membuat soal matematika secara acak."""

    daftar_soal = []
    operasi = ["+", "-", "*", "/"]

    for nomor in range(1, jumlah + 1):
        operator = random.choice(operasi)

        if operator == "+":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            jawaban = a + b

        elif operator == "-":
            a = random.randint(1, 100)
            b = random.randint(1, a)
            jawaban = a - b

        elif operator == "*":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            jawaban = a * b

        else:
            b = random.randint(1, 10)
            jawaban = random.randint(1, 20)
            a = b * jawaban

        daftar_soal.append({
            "nomor": nomor,
            "soal": f"{a} {operator} {b}",
            "jawaban": jawaban,
            "jawaban_pengguna": None,
            "status": "Belum dijawab"
        })

    return daftar_soal