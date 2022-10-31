import json

def register(type,filename,name,mobile,email,password):
    
    if type.lower()=='manager':
        details={
            "Full Name":name,
            "Mobile Number":mobile,
            "Email":email,
            "Password":password,
        }
        file = open("manager.json","r+")
        try:
            data=json.load(file)
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                file.close()
                return True
        except json.decoder.JSONDecodeError:
            print("Exception")
            lst=[]
            lst.append(data)
            json.dump(lst,file)
            file.close()
            return True
        finally:
            print("finally")
            file.close()
        return False


if __name__ == "__main__":
    register("manager","manager.json","Bharati","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Aditya","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Indresh","1234567890","bharati@gmail.com","123456")