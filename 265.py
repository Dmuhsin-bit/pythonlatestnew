# Create a method in the Book class.
# Insert a function that returns a formatted string
# with the book title and author,
# and execute it on the b1 object.

class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def book1(self):
        print(f"book title: {self.title} \nbook author:{self.author}")


b1 = book("life","illyas")
b1.book1()
