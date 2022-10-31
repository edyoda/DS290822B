# book 

# book_ID
# book_name
# book_edition
# book_author_name
# book_publication
# book_price

# functionality

# add_book()
# delete_book()
# search_book_by_ID()
# view_books()
# update_book()

class book():
    def __init__(self,book_ID,book_name,book_edition,book_author,book_publication,book_price):
        self.__book_ID = book_ID
        self.__book_name = book_name
        self.__book_edition = book_edition
        self.__book_author = book_author
        self.__book_publication = book_publication
        self.__book_price = book_price

    def __str__(self):
        return f"Book ID : {self.__book_ID} \nBook Name : {self.__book_name} \nBook Edition : {self.__book_edition} \nBook Author : {self.__book_author} \nBook Publication : {self.__book_publication} \nBook Price : {self.__book_price}"

    def set_book_ID(self,book_ID):
        self.__book_ID = book_ID

    def get_book_ID(self):
        return self.__book_ID

    def set_book_name(self,book_name):
        self.__book_name = book_name

    def get_book_name(self):
        return self.__book_name

    def set_book_edition(self,book_edition):
        self.__book_edition = book_edition

    def get_book_edition(self):
        return self.__book_edition

    def set_book_author(self,book_author):
        self.__book_author = book_author

    def get_book_author(self):
        return self.__book_author

    def set_book_publication(self,book_publication):
        self.__book_publication = book_publication

    def get_book_publication(self):
        return self.__book_publication

    def set_book_price(self,book_price):
        self.__book_price = book_price

    def get_book_price(self):
        return self.__book_price






if __name__ == "__main__":
    book_obj = book(1,"Python","I","Guido","Edyoda",500)
    print(book_obj)
