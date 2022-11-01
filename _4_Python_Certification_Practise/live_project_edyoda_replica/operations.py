import json

def register(filename,name,mobile,email,password):
    details={
            "Full Name":name,
            "Mobile Number":mobile,
            "Email":email,
            "Password":password,
        }
        
    file = open(filename,"r+")
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
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    finally:
        file.close()
    return False

def login(filename,email_id,password):
    file = open(filename,"r+")
    try:
        data = json.load(file)
        for i in data:
            if i["Email"] == email_id and i["Password"] == password:
                return True
            else:
                return False
    except json.decoder.JSONDecodeError:
        return False
    finally:
        file.close()
    return False

def create_module(filename,module_ID,module_name,start_date,end_date):
    details={
            "module_ID":module_ID,
            "module_name":module_name,
            "start_date":start_date,
            "end_date":end_date,
        }
        
    file = open(filename,"r+")
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
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    finally:
        file.close()
    return False

def view_module(filename):
    file = open(filename,"r+")
    data = json.load(file)
    return data

def update_module(filename,module_ID,module_name,start_date,end_date):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["module_ID"] == module_ID:
            data[i]["module_name"] = module_name
            data[i]["start_date"] = start_date
            data[i]["end_date"] = end_date
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False

def delete_module(filename,module_ID):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["module_ID"] == module_ID:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False

# CRUD - Create Read Update Delete


if __name__ == "__main__":
    register("manager","manager.json","Bharati","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Aditya","1234567890","bharati@gmail.com","123456")
    register("manager","manager.json","Indresh","1234567890","bharati@gmail.com","123456")