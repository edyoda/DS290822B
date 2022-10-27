class movie_ticket:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}

    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0:
                    if j == 0:
                        print(" ",end=' ')
                    else:
                        print(j,end=' ')
                elif j == 0:
                    print(i,end=' ')
                else:
                    print("S",end=' ')
            print()


    def buy_ticket(self):
        row1 = int(input("Enter the row for which you want to book the ticket : "))
        column1 = int(input("Enter the column for which you want to book the ticket : "))
        ticket_price = 10
        option = int(input(f"Your opt rows is {row1} and column is {column1},so the price for your seat is {ticket_price}.If you still wish to book the ticket please enter \n1.Yes \n.2.No \n"))
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = int(input("Enter your age : "))
            mobile_no = int(input("Enter your mobile no: "))
            seat_no = str(row1)+str(column1)
            self.user_details[seat_no] = [name,gender,age,mobile_no,seat_no]
            print("Booked Successfully!")
            print(self.user_details)
        else:
            print("No Problem! Thank You for connecting with Book My Show!!!")




