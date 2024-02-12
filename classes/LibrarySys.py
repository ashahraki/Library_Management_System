
from Library import Library
from Member import Member
from book import Book
class Librarysystem:
    def __init__(self, library:Library):
        self.library = library
        self.members = []


    
    def add_member(self, member: Member):
        self.members.append(member)

    def remove_member(self, member: Member):
        self.members.remove(member)

    def display_member_info(self, member: Member):
        if member in self.members:
            print(f"Name: {member.name}\nNumber of Borrowed Books: {member.borrowed_books}\nBalance:{member.balance}\nreturn_due_date: {member.return_due_date}")
        else:
            print(f"{member.name} Doesn't exist.")
    def display_all_member(self):
        for mmbr in self.members:
            self.display_member_info(mmbr)
    def display_library_books(self):
        for book in self.library.books:
            print(f"Title: {book.title}")
            print(f"Authors: {', '.join(book.authors)}")
            print(f"Published Year: {book.published_year}")
            print(f"Editions: {book.editions}")
