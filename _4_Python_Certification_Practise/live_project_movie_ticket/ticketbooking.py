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
                    if self.is_seat_booked(i,j):
                        print("B",end=" ")
                    else:
                        print("S",end=' ')
            print()


    def buy_ticket(self):
        row1 = int(input("Enter the row for which you want to book the ticket : ")) # 1
        column1 = int(input("Enter the column for which you want to book the ticket : "))

        total_seats = self.rows * self.columns

        if  total_seats <= 60:
            ticket_price = 10
        else:
            if row1 <= (self.rows//2): 
                ticket_price = 10
            else:
                ticket_price = 8    
        
        option = int(input(f"Your opt rows is {row1} and column is {column1},so the price for your seat is {ticket_price}.If you still wish to book the ticket please enter \n1.Yes \n.2.No \n"))
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = int(input("Enter your age : "))
            mobile_no = int(input("Enter your mobile no: "))
            seat_no = str(row1)+str(column1)
            self.user_details[seat_no] = [name,gender,age,mobile_no,ticket_price]
            print("Booked Successfully!")
        else:
            print("No Problem! Thank You for connecting with Book My Show!!!")

    def statistics(self):
        
        total_seats = self.rows * self.columns
        no_of_tickets_booked = len(self.user_details)
        percentage_of_tickets_booked =  no_of_tickets_booked/total_seats*100

        price_lst = []
        for k,v in self.user_details.items():
            price_lst.append(v[4])

        current_income = sum(price_lst)

        if  total_seats <= 60:
            total_income = total_seats * 10
        else:
            front_price = 10
            back_price = 8
            front_seats = (self.rows//2)*self.columns
            total_income = front_seats * front_price + (total_seats - front_seats) * back_price

        print(f"Number of purchased ticket : {no_of_tickets_booked} \nPecentage of ticket booked : {percentage_of_tickets_booked} \nCurrent income : {current_income} \nTotal income : {total_income}")

    def user_info(self):
        row1 = int(input("Enter the row : "))
        column1 = int(input("Enter the column : "))
        seat_no = str(row1) + str(column1)

        user_data = self.user_details.get(seat_no,None)

        if user_data:
            print(f"Name : {user_data[0]} \nGender : {user_data[1]} \nAge : {user_data[2]} \nPhone no : {user_data[3]} \nTicket price : {user_data[4]}")
        else:
            print(f"No Ticket Booked w.r.t row i.e {row1} and column i.e {column1}")

    def is_seat_booked(self,row,column):
        seat_no = str(row)+str(column)
        if seat_no in self.user_details.keys():
            return True
        return False





