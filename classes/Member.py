
from book import Book
from Library import Library
import datetime
class Member:
    def __init__(self, 
                name_member = str, 
                borrowed_books = [Book],
                balance = int):
        
        self.name = name_member
        self.borrowed_books = borrowed_books
        self.balance = balance
        self.return_due_date = {}




    ##----
    def display_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Title : {book.title}\nAuthors : {book.authors}\nPublished Year : {book.published_year}\nEdtions : {book.editions}\nRental Fee : {book.rental_fee}\n\n")
    


    def request_book(self, book:Book, bksLib:Library):
        if book in bksLib.bookslib:
            if len(self.borrowed_books) < 2:
                return True
        return False

    def borrow_book(self, bksLib:Library, book:Book):
        for bk in bksLib.bookslib:
            for ebk in bk.editions.keys():
                if ebk in book.editions.keys():
                    if bk.editions[ebk] > 0:
                        bk.editions[ebk] -=1
                        self.balance -= (bk.rental_fee)
                        self.borrowed_books.append(book)
                        curr_day = datetime.datetime.now()
                        self.return_due_date[bk] = (
                            int(curr_day.strftime("%j")) + 7
                        )
                        return
        return
    
    ## back  a book to lib
    def return_book(self, bksLib:Library, book: Book):
        for bk in bksLib.bookslib:
            for ebk in bk.editions.keys():
                if ebk in book.editions.keys():
                    bk.editions[ebk] += 1
        self.barrowed_books.remove(book)
        late_day = Member.remaining_due_days(self, book)
        late_day *= -1
        while late_day > 0:
            self.balance -= book.rental_fee * bksLib.late_fee_percentage
            late_day -= 1


    
    def remaining_due_days(self, book:Book):
        if book in self.return_due_date:
            return int(self.return_due_date[book]) - int(datetime.datetime.now().strftime("%j"))
        
    def charge_balance(self, m:int):
        self.balance += m
            

















