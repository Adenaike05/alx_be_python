class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author        
    
    def get_info(self):  
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_info(self):
        return f"Ebook: {self.title} by {self.author}, file size: {self.file_size}kB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):  # updated param name
        super().__init__(title, author)
        self.page_count = page_count  # updated attribute name

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
         self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_info())
        