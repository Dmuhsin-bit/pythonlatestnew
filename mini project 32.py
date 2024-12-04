class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, title, quantity=1):
        """Add books to the library."""
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"{quantity} copies of '{title}' added to the library.")

    def lend_book(self, title, borrower):
        """Lend a book to a borrower."""
        if title not in self.books:
            print(f"'{title}' is not available in the library.")
        elif self.books[title] > 0:
            self.books[title] -= 1
            print(f"'{title}' has been lent to {borrower}.")
        else:
            print(f"'{title}' is currently unavailable.")

    def return_book(self, title):
        """Return a borrowed book."""
        if title in self.books:
            self.books[title] += 1
            print(f"'{title}' has been returned to the library.")
        else:
            self.books[title] = 1
            print(f"'{title}' was not part of the library. Added as a new book.")

    def display_books(self):
        """Display all books in the library."""
        if self.books:
            print(f"\nBooks available in '{self.name}':")
            for title, quantity in self.books.items():
                print(f"{title}: {quantity} copies")
        else:
            print(f"The library '{self.name}' has no books.")

# Example usage
if __name__ == "__main__":
    my_library = Library("City Library")

    my_library.add_book("The Great Gatsby", 3)
    my_library.add_book("1984", 2)
    my_library.display_books()

    my_library.lend_book("The Great Gatsby", "Alice")
    my_library.lend_book("1984", "Bob")
    my_library.display_books()

    my_library.return_book("The Great Gatsby")
    my_library.display_books()

    my_library.lend_book("Moby Dick", "Charlie")
    my_library.return_book("Moby Dick")
    my_library.display_books()
