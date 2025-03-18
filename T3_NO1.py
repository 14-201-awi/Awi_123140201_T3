import math

class Kalkulator:
    def __init__(self, nilai):
        # Konstruktor untuk menyimpan nilai awal
        self.nilai = nilai

    # Operator penjumlahan (+)
    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    # Operator pengurangan (-)
    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)

    # Operator perkalian (*)
    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)

    # Operator pembagian (/)
    def __truediv__(self, other):
        if other.nilai != 0:
            return Kalkulator(self.nilai / other.nilai)
        else:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan!")  # Mencegah pembagian dengan nol

    # Operator perpangkatan (**)
    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)

    # Fungsi logaritma natural (basis e)
    def log(self):
        if self.nilai > 0:
            return math.log(self.nilai)
        else:
            raise ValueError("Log hanya untuk angka positif!")  # Logaritma tidak terdefinisi untuk nilai negatif atau nol

    # Fungsi untuk mengonversi hasil ke string (untuk mencetak output)
    def __str__(self):
        return str(self.nilai)
2
# meminta user memasukkan angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

angka1 = Kalkulator(angka1)  
angka2 = Kalkulator(angka2)   

# Operasi untuk penjumlahan
hasil_tambah = angka1 + angka2
# Operasi untuk pengurangan
hasil_kurang = angka1 - angka2
# Operasi untuk perkalian
hasil_kali = angka1 * angka2
# Operasi untuk pembagian
hasil_bagi = angka1 / angka2
# Operasi untuk perpangkatan
hasil_pangkat = angka1 ** angka2
# Operasi untuk logaritma
hasil_log = angka1.log()

# Menampilkan hasil operasi
print(f"Hasil Tambah: {hasil_tambah}")
print(f"Hasil Kurang: {hasil_kurang}")
print(f"Hasil Kali: {hasil_kali}")
print(f"Hasil Bagi: {hasil_bagi}")
print(f"Hasil Pangkat: {hasil_pangkat}")
print(f"Log dari {angka1}: {hasil_log}")