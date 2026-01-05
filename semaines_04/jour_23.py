# Library Management System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

# Library class to manage a collection of books
class Library:
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added to the library.')
        
    # View all books in the library
    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Books in the library ---")
        for book in self.books:
            book.display_info()
            print("-" * 20)

    # Borrow a book from the library
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f'You have borrowed "{title}". Enjoy reading!')
                return
        print(f'Sorry, "{title}" is either not available or already borrowed.')

    # Return a book to the library
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f'Thank you for returning "{title}".')
                return
        print(f'"{title}" was not borrowed from this library.')

# Main program loop
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == '2':
        library.view_books()
    elif choice == '3':
        title = input("Enter the title of the book to borrow: ")
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter the title of the book to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
