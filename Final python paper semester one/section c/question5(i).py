class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
#creating an instance of the class.
book = Book("Gulliver's Travel", "HM. Adams", 200)
print(book.display_info())  