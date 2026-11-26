
# ==========================================
# PROJECT UTS PEMROGRAMAN BERORIENTASI OBJEK
# SISTEM DATA MAHASISWA
# ==========================================


# CLASS 1: MAHASISWA
class Mahasiswa:

    # Attribute class
    total_mahasiswa = 0

    # Constructor
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.__nilai = 0

        self.nilai = nilai

        Mahasiswa.total_mahasiswa += 1

    # Property
    @property
    def nilai(self):
        return self.__nilai

    # Setter
    @nilai.setter
    def nilai(self, nilai_baru):
        if Mahasiswa.validasi_nilai(nilai_baru):
            self.__nilai = nilai_baru
        else:
            raise ValueError(
                "Nilai harus antara 0 sampai 100!"
            )

    # Method
    def tampilkan_data(self):
        print("NIM   :", self.nim)
        print("Nama  :", self.nama)
        print("Nilai :", self.nilai)

    # Class Method
    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    # Static Method
    @staticmethod
    def validasi_nilai(nilai):
        return 0 <= nilai <= 100


# CLASS 2: SISTEM MAHASISWA
class SistemMahasiswa:

    # Constructor
    def __init__(self):
        self.daftar_mahasiswa = []

    # Menambahkan mahasiswa
    def tambah_mahasiswa(self, nim, nama, nilai):
        try:
            mahasiswa = Mahasiswa(nim, nama, nilai)
            self.daftar_mahasiswa.append(mahasiswa)

            print("\nData berhasil ditambahkan!")

        except ValueError as error:
            print("\nGagal menambahkan data:", error)

    # Menampilkan semua mahasiswa
    def tampilkan_semua(self):
        if not self.daftar_mahasiswa:
            print("\nBelum ada data mahasiswa!")
            return

        print("\n===== DATA MAHASISWA =====")

        for mahasiswa in self.daftar_mahasiswa:
            print("-------------------------")
            mahasiswa.tampilkan_data()

    # Mengubah nilai mahasiswa
    def ubah_nilai(self, nim, nilai_baru):
        for mahasiswa in self.daftar_mahasiswa:

            if mahasiswa.nim == nim:
                try:
                    mahasiswa.nilai = nilai_baru
                    print("\nNilai berhasil diperbarui!")

                except ValueError as error:
                    print("\nGagal mengubah nilai:", error)

                return

        print("\nMahasiswa tidak ditemukan!")

    # Menghitung rata-rata
    def rata_rata(self):
        if not self.daftar_mahasiswa:
            print("\nBelum ada data mahasiswa!")
            return

        total = sum(
            mahasiswa.nilai
            for mahasiswa in self.daftar_mahasiswa
        )

        rata = total / len(self.daftar_mahasiswa)

        print("\nRata-rata nilai:", rata)


# ==========================================
# MEMBUAT OBJECT
# ==========================================

sistem = SistemMahasiswa()


# ==========================================
# MENU UTAMA
# ==========================================

while True:

    print("\n================================")
    print("      SISTEM DATA MAHASISWA")
    print("================================")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Ubah Nilai Mahasiswa")
    print("4. Hitung Rata-rata Nilai")
    print("5. Jumlah Mahasiswa")
    print("6. Keluar")
    print("================================")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":

        print("\n--- TAMBAH MAHASISWA ---")

        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        try:
            nilai = float(input("Masukkan Nilai: "))
            sistem.tambah_mahasiswa(nim, nama, nilai)

        except ValueError:
            print("\nNilai harus berupa angka!")

    elif pilihan == "2":

        sistem.tampilkan_semua()

    elif pilihan == "3":

        nim = input("Masukkan NIM: ")

        try:
            nilai_baru = float(input("Masukkan nilai baru: "))
            sistem.ubah_nilai(nim, nilai_baru)

        except ValueError:
            print("\nNilai harus berupa angka!")

    elif pilihan == "4":

        sistem.rata_rata()

    elif pilihan == "5":

        print(
            "\nJumlah mahasiswa:",
            Mahasiswa.jumlah_mahasiswa()
        )

    elif pilihan == "6":

        print("\nProgram selesai. Terima kasih!")
        break

    else:

        print("\nPilihan tidak tersedia!")
