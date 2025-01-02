from models.book import Book

class BookView:
    def show_menu(self):
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        return input("\nPilih menu (1-5): ")

    def input_book(self):
        print("\nMasukkan Data Buku:")
        try:
            code = input("Kode Buku (5 karakter): ")
            title = input("Judul Buku: ")
            author = input("Nama Penulis: ")
            year = input("Tahun Terbit: ")
            return Book(code, title, author, year)
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def display_books(self, books):
        if not books:
            print("\nBelum ada data buku")
            return

        print("\nDaftar Buku:")
        print("-" * 80)
        print(f"{'Kode':<8} {'Judul':<35} {'Penulis':<25} {'Tahun':<6}")
        print("-" * 80)
        
        for book in books:
            print(f"{book.code:<8} {book.title[:33]:<35} {book.author[:23]:<25} {book.year:<6}")
        print("-" * 80)

    def display_book(self, book):
        if book:
            print("\nDetail Buku:")
            print(f"Kode   : {book.code}")
            print(f"Judul  : {book.title}")
            print(f"Penulis: {book.author}")
            print(f"Tahun  : {book.year}")
        else:
            print("\nBuku tidak ditemukan")