class Book:
    count=0
    def __init__(self,book_name,author,price):
        self.book_name=book_name
        self.author=author
        self.price=price
        self.is_issued=False
        Book.count+=1

    
    def __str__(self):
        return f"{self.book_name} is wriiten by {self.author} and price is {self.price}"
    
    @classmethod
    def display(cls):
        return f"{cls.count}count of books in store"
    

class Library:

    def __init__(self):
        self.books=[]
    
    def add_books(self,book):
        self.books.append(book)
    
    def list_books(self):
        if not self.books:
            print("no books available")
            return
        print("Library books:")
        
        for i,book in enumerate(self.books):
            print(f"{i+1} {book}")
        

library=Library()

book1=Book("THOUSAND","John",500)
book2=Book("Thirukural","THiruvalluvar",10000)
print(book1)

library.add_books(book1)
library.add_books(book2)

library.list_books()
print(Book.display())


    
        