import json

def register(type,filename,name,mobile,email,password):
    
    if type.lower() == "manager":
        details = {
            "Name" : name,
            "Mobile No" : mobile,
            "Email" : email,
            "Password" : password
        }
        file = open(filename,"r+")
        try:
            data = []
            data = json.load(file)
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            return True
        except json.decoder.JSONDecodeError as ex:
            print(ex)
            lst = []
            lst.append(details)
            json.dump(lst,file)
        finally:
            file.close()



if __name__ == "__main__":
    register("manager","manager.json","Bharati","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Aditya","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Indresh","1234567890","bharati@gmail.com","123456")