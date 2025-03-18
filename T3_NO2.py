import random

# Kelas Father untuk menyimpan informasi golongan darah ayah
class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

# Kelas Mother untuk menyimpan informasi golongan darah ibu
class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

# Kelas Child untuk menentukan golongan darah anak berdasarkan pewarisan dari ayah dan ibu
class Child:
    def __init__(self, father, mother):
        # Mengambil alel dari ayah dan ibu, kemudian menentukan golongan darah anak
        self.blood_type = self.inherit_blood_type(father.blood_type, mother.blood_type)

    # Fungsi untuk mewarisi alel dari ayah dan ibu
    def inherit_blood_type(self, father_blood, mother_blood):
        # Mendapatkan satu alel secara acak dari ayah dan ibu
        father_allele = random.choice(father_blood)
        mother_allele = random.choice(mother_blood)
        
        # Menggabungkan alel dari ayah dan ibu untuk menentukan golongan darah anak
        return self.combine_alleles(father_allele, mother_allele)

    # Fungsi untuk menentukan golongan darah anak berdasarkan kombinasi alel
    def combine_alleles(self, father_allele, mother_allele):
        # Kombinasi golongan darah berdasarkan aturan genetika
        if father_allele == 'A' and mother_allele == 'A':
            return 'A'
        elif father_allele == 'A' and mother_allele == 'B':
            return random.choice(['A', 'AB'])  # Bisa menjadi A atau AB
        elif father_allele == 'B' and mother_allele == 'A':
            return random.choice(['B', 'AB'])  # Bisa menjadi B atau AB
        elif father_allele == 'B' and mother_allele == 'B':
            return 'B'
        elif father_allele == 'O' and mother_allele == 'A':
            return 'A'
        elif father_allele == 'A' and mother_allele == 'O':
            return 'A'
        elif father_allele == 'O' and mother_allele == 'B':
            return 'B'
        elif father_allele == 'B' and mother_allele == 'O':
            return 'B'
        elif father_allele == 'O' and mother_allele == 'O':
            return 'O'
        # Jika salah satu orang tua bergolongan darah AB, anak bisa memiliki golongan darah A, B, atau AB
        elif father_allele == 'AB' or mother_allele == 'AB':
            return random.choice(['A', 'B', 'AB'])

if __name__ == "__main__":
    # Input golongan darah dari user
    father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
    mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()

    # Membuat objek Father dan Mother berdasarkan input user
    father = Father(father_blood_type)
    mother = Mother(mother_blood_type)

    # Membuat objek Child untuk menentukan golongan darah anak
    child = Child(father, mother)

    # Menampilkan hasil golongan darah anak
    print(f"Golongan darah anak: {child.blood_type}")