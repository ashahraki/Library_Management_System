# import
import pandas as pd
import csv
import ast



class Book:
    # attribute class book
    _fbooks = 'book.csv'
    
    


    def __init__(self, title = str,
                authors = [str],
                published_year = int,
                editions = dict,
                rental_fee = float):
        
        self.title = title
        self.authors = authors
        self.published_year = published_year
        self.editions = editions
        self.rental_fee = rental_fee
        
    

    ### Display inforamtion a book
    def display_info(self):
        print(f"Title : {self.title}\nAuthors : {self.authors})\nPublished Year: {self.published_year}\nRental_fee: {self.rental_fee}\nEdition: {self.editions}")

    
    ### add eddition and stock's book
    def add_eddition(self,new_edition:dict):
        self.editions.update(new_edition)



    ### load from csv
    def load_from_csv():
        csv_books = pd.read_csv(Book._fbooks)
        print(csv_books)



    #save a book information to book.csv file
    def save_to_csv(self):
        header = ["Title", "Authors", "Published_Year", "Editions","Rental_Fee"]
        books = []
        books.append([self.title, self.authors,
                        self.published_year, self.editions, self.rental_fee])
  
        df = pd.DataFrame(books, columns= header)
        df.to_csv(self._fbooks, sep=',', index=False, mode='a', header= False)


    

    ## to calculate total rental fee a book to rented each number of days
    def calculate_rental_fee(self, rented_number_of_days:int):
        total_rental_fee = self.rental_fee * rented_number_of_days
        return total_rental_fee


## main
# edition= {"1":13, '2':43}
# newedition = {"2": 10}


# b = Book("DS", ["Ali", "ghasem"], 2021, edition, 1100)

# b.display_info()
# b.add_eddition(newedition)
# print('-------')
# b.display_info()
# # print(b)



# b2 = Book("DBMS", ["Rajaei", "Mehri"], 1312, edition, 2323)
# b.save_to_csv()
# b2.save_to_csv()



# Book.load_from_csv()
# Book.add_eddition(b, newedition)
# b.save_to_csv()
# Book.load_from_csv()