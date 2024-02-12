from book import Book
from Library import Library
from LibrarySys import Librarysystem
from Member import Member
from SpecialMember import SpecialMember

#### Main ####

# edition = {"1": 2, "2": 4}
# newedition = {"3": 3}
# b1 = Book("DS", ["Dr Ghodsi", "Dr Abam"], 2015, edition, 30)
# b2 = Book("DLD", ["Dr. Sargolzaei", "Dr Mohana"], 2021, edition, 40)
# b3 = Book("OS", ["Dr. Rajaei", "Dr. Noferesti"], 2019, edition, 25)
  
# b1.add_eddition(newedition)  # Adds new editions to the book

# b1.save_to_csv()  # Saves the book information to a CSV file

# ---------------------------
# add member

# m1 = Member("Janan", [b1], 100)
# m2 = Member("Sina", [b2,b1], 170)
# m3 = Member("Mina", [], 90)

# ---------------------------
# add book (b1,b2,b3) in library lib with late_fee_percentage 10%
# lib = Library(10)
# lib.add_book(b1)
# lib.add_book(b2)
# lib.add_book(b3)

## display all books in library lib
# lib.display_all_book()

# ---------------------------
### add member (m1,m2,m3) to list library in books list
# ll = Librarysystem(lib)
# ll.add_member(m1)
# ll.add_member(m2)
# ll.add_member(m3)




###----------

####Is Member m3 can to borrowed book b2 ? yes he/she can
# print(Member.request_book(m3, b2, lib)) #out put : True

####Is Member m2 can to borrowed book b2 ? No he/she can't
# print(Member.request_book(m2, b2, lib)) #out put : False

###----------

### Borrowed book b3 by member m3 in Library lib

# Member.borrow_book(m3, lib, b2)
# Librarysystem.display_member_info(ll, m3)

###----------


