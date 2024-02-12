from Member import Member
from LibrarySys import Librarysystem
import datetime


class SpecialMember:
    class Special_member(Member, Librarysystem):


        def __init__(self, discount_rate, *args, **kwargs):

            self.discount_rate = discount_rate
            super().__init__(*args, **kwargs)



        def apply_discount(self, discount):
            self.discount_rate = discount

        

        def borrow_book(self, bksLib , book):
            for bk in bksLib.bookslib:
                for ebk in bk.editions.keys():
                    if ebk in book.editions.keys():
                        if bk.editions[ebk] > 0:
                            bk.editions[ebk] -=1
                            self.balance -= (bk.rental_fee * self.discount_rate) / 100
                            self.borrowed_books.append(book)
                            curr_day = datetime.datetime.now()
                            self.return_due_date[bk] = (
                                int(curr_day.strftime("%j")) + 7
                            )
            
            return super().borrow_book(bksLib, book)
        

        def display_member_info(self, member: Member):
            if member in self.members:
                print(f"Name: {member.name}\nNumber of Borrowed Books: {member.borrowed_books}\nBalance:{member.balance}\nreturn_due_date: {member.return_due_date}")
            else:
                print(f"{member.name} Doesn't exist.")
            