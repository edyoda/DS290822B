from ticketbooking import movie_ticket

class Main:
    def execute(self,choice):
        if choice == 1:
            print("*******Show the seats*******")
            movie_ticket_obj.show_seats()
        if choice == 2:
            print("*******Buy Ticket*******")
            movie_ticket_obj.buy_ticket()
        if choice == 3:
            print("*******Statistics*******")
            movie_ticket_obj.statistics()
        if choice == 4:
            print("*******User Info*******")
            movie_ticket_obj.user_info()
        if choice == 0:
            print("*******Thank You for connecting with us! Good Day! Bye*******")
            exit()
            

if __name__ == "__main__":
    rows = int(input("Enter the number for rows : "))
    columns = int(input("Enter the number of seats in each rows : "))

    movie_ticket_obj = movie_ticket(rows,columns)
    obj = Main()

    while True:
        choice = int(input("Enter \n1.Show the seats \n2.Buy a ticket \n3.Statistics \n4.Show booked ticket's user info \n0.Exit : \n"))    
        obj.execute(choice)