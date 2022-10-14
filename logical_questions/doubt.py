class account:
    def __init__(self , title , balance):
        self.title = title
        self.balance = balance

    def display(self):
        print("(" , self.title , "," , self.balance , ")")

class savingsaccount(account):
    def __init__(self , title , balance , interestrate):
        super().__init__(title , balance)
        self.interestrate = interestrate

    def display(self):
        print("(" , self.title , "," , self.balance , "," , self.interestrate , ")")

title = input("Enter your name :")
balance = int(input("Enter your account balance :"))
interestrate = int(input("Enter interestrate :"))
account_obj = account()
account_obj.display()
savingsaccount_obj = savingsaccount()
savingsaccount_obj.display()
