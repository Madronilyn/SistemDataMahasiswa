# SISTEM DATA MAHASISWA
### Project Ujian Tengah Semester (UTS)
**Mata Kuliah: Pemrograman Berorientasi Objek (OOP)**

---

## 1. Deskripsi Project

Sistem Data Mahasiswa merupakan aplikasi sederhana berbasis bahasa pemrograman Python yang dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek.

Aplikasi ini dirancang untuk membantu proses pengelolaan data mahasiswa melalui antarmuka berbasis terminal (Command Line Interface).

Program ini menerapkan konsep Object-Oriented Programming (OOP), yaitu penggunaan class, object, constructor, attribute, method, encapsulation, property, setter, class method, dan static method.

## 2. Tujuan Pembuatan

Tujuan dari pembuatan aplikasi ini adalah:

- Memahami penerapan konsep Object-Oriented Programming menggunakan Python.
- Mengimplementasikan class dan object dalam sebuah program.
- Memahami penggunaan constructor, attribute, dan method.
- Menerapkan konsep encapsulation untuk melindungi data.
- Menggunakan property dan setter untuk mengatur akses serta perubahan data.
- Memahami penggunaan class method dan static method.
- Membuat aplikasi sederhana yang dapat dijalankan secara interaktif.

## 3. Fitur Aplikasi

Aplikasi Sistem Data Mahasiswa memiliki beberapa fitur utama:

| No. | Fitur | Keterangan |
|---|---|---|
| 1 | Tambah Mahasiswa | Menambahkan NIM, nama, dan nilai mahasiswa |
| 2 | Tampilkan Data | Menampilkan seluruh data mahasiswa |
| 3 | Ubah Nilai | Mengubah nilai berdasarkan NIM |
| 4 | Rata-rata Nilai | Menghitung rata-rata nilai mahasiswa |
| 5 | Jumlah Mahasiswa | Menampilkan jumlah mahasiswa yang terdaftar |
| 6 | Keluar | Mengakhiri program |

## 4. Penerapan Konsep OOP

Program ini menerapkan beberapa konsep utama Object-Oriented Programming:

### A. Class
Class merupakan cetakan untuk membuat object.

Class yang digunakan:
- `Mahasiswa`
- `SistemMahasiswa`

### B. Object
Object merupakan hasil dari class yang dibuat.

Contoh:
`SistemMahasiswa()` digunakan untuk membuat object sistem.

### C. Constructor (__init__)
Constructor digunakan untuk menginisialisasi data ketika object dibuat.

### D. Attribute dan Method
Attribute merupakan data yang dimiliki object, sedangkan method merupakan fungsi yang terdapat di dalam class.

Contoh attribute:
- nim
- nama
- nilai

Contoh method:
- tampilkan_data()
- tambah_mahasiswa()
- ubah_nilai()
- rata_rata()

### E. Encapsulation
Encapsulation diterapkan menggunakan attribute private `__nilai` agar data nilai tidak diakses secara langsung dari luar class.

### F. Property dan Setter
Property digunakan untuk mengambil nilai mahasiswa, sedangkan setter digunakan untuk mengubah nilai dengan proses validasi.

### G. Class Method
Class method digunakan untuk menghitung jumlah mahasiswa melalui attribute class `total_mahasiswa`.

### H. Static Method
Static method digunakan untuk melakukan validasi nilai mahasiswa, yaitu memastikan nilai berada dalam rentang 0 sampai 100.

## 5. Teknologi yang Digunakan

- Bahasa Pemrograman: Python
- Versi Python: 3.13.14
- Code Editor: Visual Studio Code
- Platform Penyimpanan: GitHub
- Jenis Aplikasi: Command Line Interface (CLI)

## 6. Struktur Project

```text
SistemDataMahasiswa/
│
├── main.py
└── README.md
```

Keterangan:
- `main.py`: File utama yang berisi seluruh kode program.
- `README.md`: Dokumentasi dan penjelasan project.

## 7. Cara Menjalankan Program

Ikuti langkah-langkah berikut:

1. Pastikan Python sudah terinstal di komputer.
2. Download atau clone repository ini.
3. Buka folder project menggunakan Visual Studio Code.
4. Buka terminal pada VS Code.
5. Jalankan perintah berikut:

```bash
python main.py
```

6. Program akan menampilkan menu utama Sistem Data Mahasiswa.
7. Pilih menu sesuai kebutuhan.

## 8. Contoh Penggunaan Program

Contoh menambahkan data mahasiswa:

```text
Pilih menu (1-6): 1

Masukkan NIM   : 001
Masukkan Nama  : Andi
Masukkan Nilai : 85

Data mahasiswa berhasil ditambahkan!
```

Contoh menampilkan data:

```text
===== DATA SELURUH MAHASISWA =====

NIM   : 001
Nama  : Andi
Nilai : 85
```

Contoh menghitung rata-rata:

```text
Rata-rata nilai mahasiswa: 85.0
```

## 9. Validasi Data

Program memiliki validasi nilai mahasiswa dengan ketentuan:

- Nilai minimal adalah 0.
- Nilai maksimal adalah 100.
- Nilai di luar rentang tersebut akan ditolak.
- Input nilai harus berupa angka.

Validasi dilakukan menggunakan static method dan setter.

## 10. Kesimpulan

Sistem Data Mahasiswa merupakan project sederhana yang menerapkan konsep Object-Oriented Programming menggunakan Python.

Melalui project ini, konsep dasar OOP dapat diterapkan secara langsung dalam pembuatan aplikasi, mulai dari penggunaan class dan object hingga encapsulation, property, setter, class method, dan static method.

Project ini diharapkan dapat meningkatkan pemahaman mengenai penerapan pemrograman berorientasi objek dalam menyelesaikan permasalahan sederhana.

---

**Dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS)**

Mata Kuliah: Pemrograman Berorientasi Objek  
Program Studi: Ilmu Komputer  
Kelas: 3C KOM  
Tahun Akademik: 2026/2027
