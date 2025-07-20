class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_issued=False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class library:
    def __init__(self):
        self.books=[]
    
    def add_books(self,title,author):
        book=Book(title,author)
        self.books.append(book)
        print(f"Books added:{book.title}by{book.author}")
    
    def display(self):
        if not self.books:
            print("no books available")
            return
        print("Library Books:")
        for i,book in enumerate(self.books):
            print(f"{i+1}.{book}")
    
    def borrowbooks(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                if book.is_issued:
                     print(" Book already issued.")
                else:
                    book.is_issued = True
                    print(f" You've borrowed: {book.title}")
                return
        print(" Book not found.")

library1=library()
library1.add_books("Thousands","john")
library1.display()

