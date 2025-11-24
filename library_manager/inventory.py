#Task 2: Inventory Management

import csv
from library_manager.book import Book


class LibraryInventory:
    def __init__(self):
        self.filename = 'sample.csv'
        self.books = []
        self.load_sample()

    def load_sample(self):
        try:
            with open(self.filename, 'r', newline = '') as f:
                r = csv.DictReader(f)
                for row in r:
                    self.books.append(Book(row["title"], row["author"], row["isbn"], row["status"]))
        except FileNotFoundError:
            self.books = []
        except Exception as e:
            self.books = []
            print(f"Some error arised: {e}")

    def save_sample(self):
        try:
            with open(self.filename, 'a', newline = '') as s:
                fields = ['title', 'author', 'isbn', 'status']
                w = csv.DictWriter(s, fieldnames = fields)
                for book in self.books:
                    w.writerow(book.to_dict())
        except Exception as e:
            print(f"Some error arised: {e}")


    def add_book(self, book):
        self.books.append(book)
        self.save_sample()
        

    def search_by_title(self, title):
        data = []
        for book in self.books:
            if book.title.lower() == title.lower():
                data.append(book)
        return data
    
    
    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def display_all(self):
        return self.books
    










    
 
   
        
  

        



            