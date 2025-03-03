import pickle

# Display welcome title:
print("\nWelcome to the Library Management System Ávila Cazorla 3000\n")

# Define the Book class:


class Book:
    def __init__(self, title, author, isbn):
        # Initialize book attributes:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Initially, the book is available.

    def lend(self):
        # Create a method to lend the book:
        if self.available:
            self.available = False
            print(f'The book "{self.title}" has been lent out.')
        else:
            print(f'The book "{self.title}" is already lent out.')

    def return_book(self):
        # Create a method to return the book:
        if not self.available:
            self.available = True
            print(f'The book "{self.title}" has been returned.')
        else:
            print(f'The book "{self.title}" was already available.')

# Define the InventoryManagement class:


class InventoryManagement:
    def __init__(self):
        # Initialize the list of books
        self.books = []

    def add_book(self, title, author, isbn):
        # Create a method to add a new book
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f'Book added successfully.')

    def show_books(self):
        # Create a method to show all books in the database
        for book in self.books:
            status = "Available" if book.available else "Lent Out"
            print(
                f'Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}')

    def search_book(self, isbn):
        # Method to search for a book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                status = "Available" if book.available else "Lent Out"
                print(
                    f'Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}')
                return book
        print(f'The book with ISBN {isbn} is not in the database.')
        return None

    def lend_book(self, isbn):
        # Method to lend a book by ISBN
        book = self.search_book(isbn)
        if book:
            book.lend()

    def return_book_by_isbn(self, isbn):
        # Method to return a book by ISBN
        book = self.search_book(isbn)
        if book:
            book.return_book()

    def save_data(self, filename):
        # Method to save data to a file
        with open(filename, 'wb') as file:
            pickle.dump(self.books, file)
        print(f'Data saved to {filename}.')

    def load_data(self, filename):
        # Method to load data from a file
        try:
            with open(filename, 'rb') as file:
                self.books = pickle.load(file)
            print(f'Data loaded from {filename}.')
        except FileNotFoundError:
            print(
                f'The file {filename} was not found. Starting with an empty library.')

# Implement the menu with a while loop


def menu():
    inventory = InventoryManagement()
    inventory.load_data('library.pkl')
    while True:
        # Display menu options
        print("\nMenu:")
        print("1) Add new book")
        print("2) Lend book")
        print("3) Return book")
        print("4) Show books in the database")
        print("5) Search for a book by ISBN")
        print("6) Save and exit the program\n")
        option = input("Choose an option: ").strip()

        # Create if statements to choose between menu options
        if option == '1':
            title = input("\nTitle: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(title, author, isbn)
        elif option == '2':
            isbn = input("ISBN of the book to lend: ")
            inventory.lend_book(isbn)
        elif option == '3':
            isbn = input("ISBN of the book to return: ")
            inventory.return_book_by_isbn(isbn)
        elif option == '4':
            inventory.show_books()
        elif option == '5':
            isbn = input("ISBN of the book to search: ")
            inventory.search_book(isbn)
        elif option == '6':
            inventory.save_data('library.pkl')
            print("\nExiting Ávila Cazorla 3000. Thank you for using it.")
            break
        else:
            print("\nPlease choose an option from the menu.")


# Execute the main menu
if __name__ == "__main__":
    menu()
