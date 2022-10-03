# str1 = "Bharati" - take str input from user
# {"B":1,"h":1,"a":2,"r":1,"t":1,"i":1}

str = input("Enter a string : ")
dict1 = {i:str.count(i) for i in str} 
print(dict1)
