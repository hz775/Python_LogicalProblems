class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.book_id} | {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def addbooks(self, book_id, title, author):
        for b in self.books:
            if b.book_id == book_id:
                return f"Book ID {book_id} already exists."
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        return f"'{title}' added to the library."

    def borrowbooks(self, book_id):
        for book in self.books:
            print(f"Checking book ID: {book.book_id}")  # Debug
            if book.book_id == book_id:
                if book.is_borrowed:
                    return f"'{book.title}' is already borrowed."
                book.is_borrowed = True
                return "Borrowed"
        return f"Book ID {book_id} not found."

    def returnbooks(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    return f"'{book.title}' was not borrowed."
                else:
                    book.is_borrowed = False
                    return "Returned"
        return f"Book ID {book_id} not found."

    def listbooks(self):
        if not self.books:
            return "No books available."
        return "\n".join(book.display() for book in self.books)


lib = Library()

lib.addbooks(1, "The Alchemist", "Paulo Coelho")
lib.addbooks(2, "1984", "George Orwell")
lib.listbooks()
lib.borrowbooks(1)
lib.listbooks()
lib.returnbooks(1)
lib.listbooks()
