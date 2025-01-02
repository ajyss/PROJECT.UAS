## PROJECT UAS

# LIBRARY SYSTEM


# DATA DIRI


Nama: Muhammad Aziz Tri Ramadhan 

NIM: 312410380

Kelas: TI.24.A3



# PENJELASAN TENTANG PROGRAM

1. **Struktur Program**
Program ini menggunakan arsitektur MVC (Model-View-Controller) yang dimodifikasi menjadi MVS (Model-View-Service):
```
library_system/
├── models/      # Menyimpan definisi data/objek
├── services/    # Menangani logika bisnis
├── views/       # Menangani tampilan dan input user
└── main.py      # Program utama
```

2. **Model (models/book.py)**
```python
class Book:
    def __init__(self, code, title, author, year):
        self.code = code
        self.title = title
        self.author = author
        self.year = year
```
- Kelas `Book` merepresentasikan data buku
- Memiliki method `to_dict()` untuk mengubah objek ke dictionary (untuk penyimpanan JSON)
- Memiliki method `from_dict()` untuk membuat objek dari dictionary (saat membaca JSON)

3. **Service (services/book_service.py)**
```python
class BookService:
    def __init__(self):
        self.filename = "books.json"
        self.books = self.load_books()
```
Fungsi-fungsi utama:
- `load_books()`: Membaca data buku dari file JSON
- `save_books()`: Menyimpan data buku ke file JSON
- `validate_book()`: Memvalidasi data buku:
  - Kode harus 5 karakter alfanumerik
  - Judul tidak boleh kosong
  - Penulis tidak boleh kosong
  - Tahun harus antara 1900-2024
  - Kode buku tidak boleh duplikat
- `add_book()`: Menambah buku baru
- `get_all_books()`: Mengambil semua data buku
- `get_book_by_code()`: Mencari buku berdasarkan kode
- `delete_book()`: Menghapus buku berdasarkan kode

4. **View (views/book_view.py)**
```python
class BookView:
    def show_menu(self)
    def input_book(self)
    def display_books(self, books)
    def display_book(self, book)
```
- `show_menu()`: Menampilkan menu utama
- `input_book()`: Meminta input data buku baru
- `display_books()`: Menampilkan daftar semua buku
- `display_book()`: Menampilkan detail satu buku

5. **Program Utama (main.py)**
```python
def main():
    service = BookService()
    view = BookView()
```
Menu program:
1. Tambah Buku
   - Meminta input data buku
   - Validasi data
   - Simpan ke JSON
2. Lihat Semua Buku
   - Tampilkan dalam format tabel
3. Cari Buku
   - Cari berdasarkan kode
   - Tampilkan detail buku
4. Hapus Buku
   - Hapus buku berdasarkan kode
5. Keluar

6. **Fitur Penting:**
- **Persistensi Data**
  - Data disimpan dalam file JSON
  - Data dapat dibaca kembali saat program dijalankan ulang

- **Validasi Data**
  - Kode buku (5 karakter alfanumerik)
  - Judul dan penulis (tidak boleh kosong)
  - Tahun (1900-2024)
  - Pengecekan duplikasi kode

- **Penanganan Error**
  - Try-except untuk operasi file
  - Validasi input pengguna
  - Pesan error yang informatif

7. **Cara Penggunaan:**
```bash
# Jalankan program
python main.py

# Input buku baru
1
Masukkan kode: ABC12
Masukkan judul: Python Programming
Masukkan penulis: John Doe
Masukkan tahun: 2023

# Lihat daftar buku
2

# Cari buku
3
Masukkan kode: ABC12

# Hapus buku
4
Masukkan kode: ABC12
```

8. **Pengembangan Lebih Lanjut:**
- Menambah fitur pencarian berdasarkan judul/penulis
- Menambah fitur edit buku
- Menambah fitur kategori buku
- Menambah fitur peminjaman
- Implementasi database SQL
- Menambah GUI

Program ini menerapkan prinsip:
- Separation of Concerns (pemisahan tanggung jawab)
- Single Responsibility Principle (setiap kelas memiliki satu tugas)
- Data Validation (validasi input)
- Error Handling (penanganan error)
- Data Persistence (penyimpanan data)

Apakah ada bagian tertentu yang ingin Anda ketahui lebih detail?