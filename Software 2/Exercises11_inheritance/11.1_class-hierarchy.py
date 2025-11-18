class Publication:

    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"This Publication is called {self.name}")

class Book(Publication):

    def __init__(self, name, author, pagecount):
        self.author = author
        self.pagecount = pagecount
        super().__init__(name) #super calls the upper class

    def print_information(self):
        super().print_information()
        print(f"It is a book written by {self.author} with a total of {self.pagecount} pages.")

class Magazine(Publication):

    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name) #super calls the upper class

    def print_information(self):
        super().print_information()
        print(f"It is a magazine with {self.chief_editor} as a chief editor.")

publications = []
pub1 = Publication("Dune")
pub2 = Book("Twilight", "Stephenie Meyer",544 )
pub3 = Magazine("Vogue", "Anna Wintour")


publications.append(pub1)
publications.append(pub2)
publications.append(pub3)

for e in publications:
    e.print_information()

#subclasses inherited from the base class


