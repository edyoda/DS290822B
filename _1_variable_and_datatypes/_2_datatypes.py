# int
# immutable
# non-iterable
# num = 10    

# float
# immutable
# non-iterable
# salary = 9000.67                            

# str
# immutable
# iterable
# name = "Bharati"                            

# bool
# immutable
# non-iterable
# night = True                                

# complex
# immutable
# non-iterable
# comp = 2+3j                                 

# None
# immutable
# non-iterable
# data = None                                 

# print(type(num))

# salary_type = type(salary)
# print(salary_type)

# name_type = type(name)
# print(name_type)

# night_type = type(night)
# print(night_type)

# comp_type = type(comp)
# print(comp_type)

# data_type = type(data)
# print(data_type)



# list
# are used to store more than one value
# []
# indexed - starts with 0
# it allows you to store heterogenous data (values of different datatype)
# duplicate values are allowed
# mutable (modifiable)
# list()
# ordered - it considers the same order in the order which you inserted the value in list
# iterable

# lst = [4,5,6,7,4,2,9.7,"Bharati","a",True,9] # 4-0 , 5-1, 6-2
# print(lst)

# print(lst[5])

# lst[0] = "Ram"
# print(lst)

# lst1 = list([1,2,3,4])
# print(lst1[3])

# print("lst type : ",type(lst))
# print("lst1 type : ",type(lst1))



# tuple
# are used to store more than one value
# ()
# tuple()
# allows you to store heterogenous data
# indexed
# ordered
# iterable 
# duplicates are allowed
# immutable (cannot modify)

# tup = (1,2,70,10,20,"A",True,20)
# print(tup)
# print(tup[0])

# tup[0] = "Bharati"

# # tup1 = tuple((1,2,3))
# # print(tup1)




# set
# {}
# set()
# are used to store more than one value
# iterable
# unordered
# does not allow duplicate values
# non-indexed
# mutable
# it allows heterogenous data

# set_demo = {1,10,8,4,100,2,75,10,0,"Bharati",True}
# print(set_demo)






# dict (dictionary)
# {}
# dict()
# {key:value} - item
# key - duplicates are not allowed
# values - duplicates are allowed
# unordered
# non-indexed
# it allows heterogenous data
# iterable
# mutable

# students = {1:"Bharati","a":567,3:"Laxman",10:"Bharati"}
# print(students)

# print(students[3])

# students[1] = "Edyoda"
# print(students)