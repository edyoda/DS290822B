div = 0
no1 = "90"
no2 = "89"
try:
    div = no1/no2
except Exception as ex:
    print(ex)
    no1 = int(no1)
    no2 = int(no2)
    div = no1/no2
    
print("Division : ",div)