# # Take a word from user and give vowels in output

# str1 = input("Enter a word :")
# vowels = ["A" , "E" , "I" , "O" , "U" , "a" , "e" , "i" , "o" , "u"]
# vowels_lst = []
# for i in str1:
#     if i in vowels:
#         vowels_lst.append(i)

# print("Vowels = " , vowels_lst)


str1 = input("Enter a string : ")
vowels =['A','a','E','e','I','i','O','o','U','u']
data={i for i in str1 if i in vowels}
lst=list(data)
print(lst)
