class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author        
    
    def __str__(self):  
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author}, file size: {self.file_size}kB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):  # updated param name
        super().__init__(title, author)
        self.page_count = page_count  # updated attribute name

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(f"Error: Cannot add non-Book object to the library: {book}")
    
    def list_books(self):

        if not self.books:
            print("The library is currently empty.")
            return
       
        for book in self.books:
            print(book)