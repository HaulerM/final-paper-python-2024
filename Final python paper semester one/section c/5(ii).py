class EBook:
    def __init__(self, title, author, format):
        self.title = title
        self.author = author
        self.format = format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Format: {self.format}"

    
#an instance of an Ebook class
ebook = EBook("Gulliver's Travels", "HM. Adams", "PDF")
print(ebook.display_info())
