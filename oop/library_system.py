class Book:

    def __init__(self, title: str, author: str):

        self.title = title
        self.author = author

    def __str__(self) -> str:

        return f"Book: {self.title} by {self.author}"
class EBook(Book):

    def __init__(self, title: str, author: str, file_size: int):

        super().__init__(title, author)  # Call the base class (Book) constructor
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        
        super().__init__(title, author)  # Call the base class (Book) constructor
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            # No print statement here, as per expected output
        else:
            print(f"Error: Cannot add non-Book object to the library: {book}")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
            return
        for book in self.books:
            print(book)
