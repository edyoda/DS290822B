# num = int(input("Enter a number :"))
# str1 = str(num) # 123
# lst1 = []
# for i in str1:
#     lst1.append(i) # ["1","2","3"]
# for j in lst1:
#     if j == "1":
#         print("One", end = " ")
#     if j == "2":
#         print("Two", end = " ")
#     if j == "3":
#         print("Three", end = " ")
#     if j == "4":
#         print("Four", end = " ")
#     if j == "5":
#         print("Five", end = " ")
#     if j == "6":
#         print("Six", end = " ")
#     if j == "7":
#         print("Seven", end = " ")
#     if j == "8":
#         print("Eight", end = " ")
#     if j == "9":
#         print("Nine", end = " ")
#     if j == "0":
#         print("Zero", end = " ")



num=int(input("Enter a number : ")) # 345
str1=str(num) # "345"
d={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
data=[d[i] for i in str1] # ["Three", "Four", "Five"]
for j in data:
    print(j,end=" ")
print()
