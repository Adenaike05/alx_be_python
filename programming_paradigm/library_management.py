class Book:
    
    def __init__(self, title, author):
     
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Book title cannot be empty.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Book author cannot be empty.")

        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
       
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
       
        return not self._is_checked_out

    def __str__(self):
       
        return f"{self.title} by {self.author}"


class Library:
   
    def __init__(self):
      
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        
        if not isinstance(book, Book):
            raise TypeError("Only instances of Book can be added to the library.")
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
       
        found_book = None
        for book in self._books:
            if book.title == title:
                found_book = book
                break

        if found_book:
            if found_book.check_out():
                print(f"Successfully checked out '{title}'.")
                return True
            else:
                print(f"'{title}' is already checked out.")
                return False
        else:
            print(f"'{title}' not found in the library.")
            return False

    def return_book(self, title):
       
        found_book = None
        for book in self._books:
            if book.title == title:
                found_book = book
                break

        if found_book:
            if found_book.return_book():
                print(f"Successfully returned '{title}'.")
                return True
            else:
                print(f"'{title}' is already available (not checked out).")
                return False
        else:
            print(f"'{title}' not found in the library.")
            return False

    def list_available_books(self):
       
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0:
            print("No books currently available.")