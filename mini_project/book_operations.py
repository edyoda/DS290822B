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
        book_operations.booklist.append(book_obj)
        print("Successfully Added")

    def view_book(self):
        print("*********All Books*******")
        for books in book_operations.booklist:
            print(books,"\n")

    def search_book_by_ID(self,book_ID):
        pass
        # for books in book_operations.booklist:
        #     print(books)
        #     if books.__book_ID == book_ID:
        #         return books

    def delete_book(self):
        pass

    def update_book(self):
        pass