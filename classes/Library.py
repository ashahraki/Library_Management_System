
from book import Book

class Library():
    ### Fields
    def __init__(self,
                 late_fee_percentage = None):
        self.late_fee_percentage = late_fee_percentage
        self.bookslib = []

    

    ### Methods
    def add_book(self, book:Book):
        self.bookslib.append(book)


    def remove_book(self, bk:Book):
        self.books.remove(bk)
          


    def search_books_by_author(self, author):
        for bk in self.bookslib:
            for aut in bk.authors:
                if aut == author:
                    return bk


    def display_all_book(self):
        
        for bk in self.bookslib:
            print(f"Title : {bk.title}\nAuthors : {bk.authors})\nPublished Year: {bk.published_year}\nRental_fee: {bk.rental_fee}\nEdition: {bk.editions}\n\n")



#main test
# lib = Library(12)
# edition= {"1":13, '2':43}
# b = Book("DS", ["Ali", "ghasem"], 2021, edition, 1100)
# b2 = Book("DS", ["Ali", "ghasem"], 2021, edition, 1100)
# b3 = Book("DS", ["Ali", "ghasem"], 2021, edition, 1200)
# b4 = Book("DS", ["Ali", "ghasem"], 2021, edition, 1100)
# lib.add_book(b)
# lib.add_book(b2)
# lib.add_book(b3)
# lib.add_book(b4)
# lib.display_all_book()



