import re
from operations import *
import random

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

            if register_choice == 1:
                name = input("Enter your name : ")                
                mobile = input("Enter your mobile : ")
                email = input("Enter your email : ")                
                password = input("Enter your password : ")                

                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and mobile_re and email_re and password_re:
                    flag = register("manager.json",name,mobile,email,password)
                    
                    if flag:
                        print("Successfully Registered!")
                    else:
                        print("Registeration Unsuccessful")
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

            if register_choice == 2:
                name = input("Enter your name : ")                
                mobile = input("Enter your mobile : ")
                email = input("Enter your email : ")                
                password = input("Enter your password : ")                

                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and mobile_re and email_re and password_re:
                    flag = register("student.json",name,mobile,email,password)
                    
                    if flag:
                        print("Successfully Registered!")
                    else:
                        print("Registeration Unsuccessful")
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

            if register_choice == 3:
                print("***Bye****")
                exit()
        
        if choice == 2:
            login_choice = int(input("Enter \n1.Login as Admin \n2.Login Student \n3.Exit : \n"))
            if login_choice == 1:
                email_id = input("Enter your email ID : ")
                password = input("Enter your password : ")
                flag = login("manager.json",email_id,password)
                if flag:
                    print("Login Successful")
                    while True:
                        admin_choice = int(input("Enter \n1.Create Module \n2.View Module \n3.Update Module \n4.Delete Module : \n"))
                        # Create Module
                        if admin_choice == 1:
                            
                            module_ID = random.randint(10000,20000)
                            module_name = input("Enter Module Name : ")
                            start_date  = input("Enter Start Date (YYYY-MM-DD) : ")
                            end_date  = input("Enter End Date (YYYY-MM-DD) : ")

                            if module_ID and module_name and start_date and end_date:
                                flag = create_module("module.json",module_ID,module_name,start_date,end_date)
                                if flag:
                                    print("Module is added successfully")
                                else:
                                    print("Module did not get added")
                        # View Module
                        if admin_choice == 2:
                            data = view_module("module.json")
                            for i in data:
                                print(i)

                        # Update Module
                        if admin_choice == 3:
                            module_ID = int(input("Enter Module ID : "))
                            module_name = input("Enter new Module Name : ")
                            start_date  = input("Enter new Start Date (YYYY-MM-DD) : ")
                            end_date  = input("Enter new End Date (YYYY-MM-DD) : ")

                            flag = update_module("module.json",module_ID,module_name,start_date,end_date)
                            if flag:
                                print("Module Updated")
                            else:
                                print("Module did not get updated!")

                        # Delete Module
                        if admin_choice == 4:
                            module_ID = int(input("Enter Module ID : "))
                            flag = delete_module("module.json",module_ID)
                            if flag:
                                print("Module Deleted")
                            else:
                                print("Module did not get deleted!")
                else:
                    print("Login Unsuccessful")

