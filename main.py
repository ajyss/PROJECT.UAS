import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.book_service import BookService
from views.book_view import BookView

def main():
    service = BookService()
    view = BookView()

    while True:
        choice = view.show_menu()

        if choice == '1':
            book = view.input_book()
            if book:
                try:
                    if service.add_book(book):
                        print("\nBuku berhasil ditambahkan!")
                    else:
                        print("\nGagal menyimpan buku")
                except ValueError as e:
                    print(f"\nError: {str(e)}")

        elif choice == '2':
            view.display_books(service.get_all_books())

        elif choice == '3':
            code = input("\nMasukkan kode buku: ")
            book = service.get_book_by_code(code)
            view.display_book(book)

        elif choice == '4':
            code = input("\nMasukkan kode buku yang akan dihapus: ")
            if service.delete_book(code):
                print("\nBuku berhasil dihapus!")
            else:
                print("\nBuku tidak ditemukan")

        elif choice == '5':
            print("\nTerima kasih telah menggunakan program ini!")
            break

        else:
            print("\nMenu tidak valid!")

if __name__ == "__main__":
    main()