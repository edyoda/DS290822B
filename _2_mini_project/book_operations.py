from book import book

class book_operations:

    booklist = []

    def add_book(self):
        print("*********Add Book*******")
        book_ID = int(input("Enter book ID : "))
        book_name = input("Enter book name : ")
        book_edition = int(input("Enter book edition : "))
        book_author = input("Enter book author : ")
        book_publication = input("Enter book publication : ")
        book_price = float(input("Enter book price : "))
        book_obj = book(book_ID,book_name,book_edition,book_author,book_publication,book_price)
        self.booklist.append(book_obj)
        print("Successfully Added")

    def view_book(self):
        print("*********All Books*******")
        for books in self.booklist:
            print(books,"\n")

    def search_book_by_ID(self,book_ID):
        for books in self.booklist:
            if books.get_book_ID() == book_ID:
                return books
        
        print("No such Book ID Found!!")
        return

    def delete_book(self):
        print("*******Delete Book******")
        try:
            book_ID = int(input("Enter book ID : "))
            book = self.search_book_by_ID(book_ID)
            if book:
                self.booklist.remove(book)
                print("Successfully Deleted")
        except Exception as ex:
            print(ex)

    def update_book(self):
        print("*******Update Book*******")
        book_ID = int(input("Enter book ID : "))
        book = self.search_book_by_ID(book_ID)
        if book:
            book_name = input("Enter book name : ")
            book_edition = int(input("Enter book edition : "))
            book_author = input("Enter book author : ")
            book_publication = input("Enter book publication : ")
            book_price = float(input("Enter book price : "))

            book.set_book_name(book_name)
            book.set_book_edition(book_edition)
            book.set_book_author(book_author)
            book.set_book_publication(book_publication)
            book.set_book_price(book_price)

            print("Successfully Updated")