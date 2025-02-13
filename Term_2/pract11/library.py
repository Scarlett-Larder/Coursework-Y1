class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"{self.title} | Author: {self.author} | ISBN: {self.isbn}"

class DigitalBook(Book):

    compat_options = {'Kindle', 'PDF', 'Apple'}

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.compatibility = {'Kindle'}
        self.options = set()

    def add_compat(self):
        print(f"Compatiblity: {self.compat_options}")
        wow = input("Please enter a newly compatible device: ")
        if wow not in self.compat_options:
            print("Sorry! Not an option")
        else:
            self.compatibility.add(wow)
            print(f"New compatibility: {self.compatibility}")

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def __str__(self):
        return f"{self.title} | Author: {self.author} | ISBN: {self.isbn} | Compatibility: {self.compatibility}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True

    def __str__(self):
        return "\n".join(f"{book.title}: {book.author}, {book.isbn} | {book.available}" for book in self.books)



def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    # Try the methods of the Book class here and print the book object


def test_digital_book():
    digital_book = DigitalBook(
        'Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    # Try the methods here and print it


def test_library():

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("Jane Eyre", "Charlotte Bronte", "978-0141441146")
    book4 = DigitalBook("1984", "George Orwell", "978-0451524935")

    library = Library()

    library.add_book(book1)
    library.borrow_book("The Great Gatsby")
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    print(library)