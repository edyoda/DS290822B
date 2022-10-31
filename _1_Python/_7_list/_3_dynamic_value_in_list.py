size = int(input("Enter the size of elements you want in your list : "))

lst = []
for i in range(size):
    element = int(input("Enter element : "))
    lst.append(element)

print(lst)
