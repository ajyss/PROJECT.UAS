import json
import os
from models.book import Book

class BookService:
    def __init__(self):
        self.filename = "books.json"
        self.books = self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except:
            return []

    def save_books(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
            return True
        except:
            return False

    def validate_book(self, book):
        if not book.code or len(book.code) != 5 or not book.code.isalnum():
            raise ValueError("Kode buku harus 5 karakter alfanumerik")

        if not book.title.strip():
            raise ValueError("Judul buku tidak boleh kosong")

        if not book.author.strip():
            raise ValueError("Nama penulis tidak boleh kosong")

        try:
            year = int(book.year)
            if year < 1900 or year > 2025:
                raise ValueError
        except ValueError:
            raise ValueError("Tahun harus antara 1900-2025")

        if any(b.code == book.code for b in self.books):
            raise ValueError(f"Buku dengan kode {book.code} sudah ada")

    def add_book(self, book):
        self.validate_book(book)
        self.books.append(book)
        return self.save_books()

    def get_all_books(self):
        return self.books

    def get_book_by_code(self, code):
        return next((book for book in self.books if book.code == code), None)

    def delete_book(self, code):
        book = self.get_book_by_code(code)
        if book:
            self.books.remove(book)
            return self.save_books()
        return False