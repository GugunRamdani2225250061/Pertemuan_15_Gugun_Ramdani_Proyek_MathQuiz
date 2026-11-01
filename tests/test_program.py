
import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from generator import buat_soal
from evaluasi import (
    periksa_jawaban,
    hitung_nilai,
    buat_evaluasi
)


class TestMathQuiz(unittest.TestCase):

    def test_generator(self):
        soal = buat_soal(10)
        self.assertEqual(len(soal), 10)

    def test_pemeriksaan_jawaban(self):
        data = [{
            "soal": "20 + 5",
            "jawaban": 25,
            "jawaban_pengguna": 25,
            "status": "Belum dijawab"
        }]

        hasil = periksa_jawaban(data)
        self.assertEqual(hasil[0]["status"], "Benar")

    def test_hitung_nilai(self):
        data = [
            {"status": "Benar"},
            {"status": "Benar"},
            {"status": "Salah"},
            {"status": "Benar"}
        ]

        self.assertEqual(hitung_nilai(data), 75)

    def test_data_kosong(self):
        self.assertEqual(hitung_nilai([]), 0)

    def test_evaluasi(self):
        self.assertEqual(
            buat_evaluasi(90),
            "Sangat Baik"
        )

    def test_jawaban_salah(self):
        data = [{
            "soal": "10 + 5",
            "jawaban": 15,
            "jawaban_pengguna": 10,
            "status": "Belum dijawab"
        }]

        hasil = periksa_jawaban(data)
        self.assertEqual(hasil[0]["status"], "Salah")


if __name__ == "__main__":
    unittest.main()