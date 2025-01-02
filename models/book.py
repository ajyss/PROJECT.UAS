class Book:
    def __init__(self, code, title, author, year):
        self.code = code
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {
            "code": self.code,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
    def from_dict(data):
        return Book(
            data["code"],
            data["title"],
            data["author"],
            data["year"]
        )