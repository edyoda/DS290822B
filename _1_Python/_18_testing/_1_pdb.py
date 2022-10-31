import pdb

def addition(no1,no2):
    add = no1 / no2
    return add

# pdb.set_trace()                       # 1 way to run the script in debugger mode
if __name__ == "__main__":
    no1 = input("Enter no1 : ")
    no2 = input("Enter no2 : ")
    data = addition(no1,no2)
    print(data)


# python -m pdb .\_1_pdb.py              ---> second way to run the script in debugger mode