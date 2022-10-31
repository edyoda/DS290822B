import re
from operations import *


if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Enter \n1.Register \n2.Login \n3.Exit \n"))
        except ValueError:
            print("Please enter valid choice!")
            continue

        if choice == 1:
            try:
                register_choice = int(input("Enter \n1.Register as Admin \n2.Register as Student \n3.Exit \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if register_choice:
                name = input("Enter your name : ")                
                mobile = input("Enter your mobile : ")
                email = input("Enter your email : ")                
                password = input("Enter your password : ")                

                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and mobile_re and email_re and password_re:
                    flag = register("manager","manager.json",name,mobile,email,password)
                    
                    if flag:
                        print("Successfully Added")
                    else:
                        print("Failed to add the details")
                else:
                    if not name_re:
                        print("Entered name format is incorrect")
                        continue
                    if not mobile_re:
                        print("Entered name format is incorrect")
                        continue
                    if not email_re:
                        print("Entered name format is incorrect")
                        continue
                    if not password_re:
                        print("Entered name format is incorrect")
                        continue
