from book_operations import book_operations

class main_class:

    def __init__(self):
        self.book_operations = book_operations()

    def execute(self,choice):
        if choice == 1:
            self.book_operations.add_book()
        elif choice == 2:
            self.book_operations.view_book()
        elif choice == 3:
            book_ID = int(input("Enter book ID : "))
            book = self.book_operations.search_book_by_ID(book_ID)
            print(book)
        elif choice == 4:
            self.book_operations.delete_book()
        elif choice == 5:
            self.book_operations.update_book()
        
if __name__ == "__main__":
    
    obj = main_class()

    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Search Book By ID \n4.Delete Book \n5.Update Book : \n"))
        if choice > 5 or choice < 1:
            break
        obj.execute(choice)
        