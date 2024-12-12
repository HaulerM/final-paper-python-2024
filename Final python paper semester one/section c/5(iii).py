class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"#It will return the authour and the title only.
