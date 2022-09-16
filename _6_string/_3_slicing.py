# Slicing Operator
# syntax : [start_range : end_range : step]
# it is used to get the substring from string

str1 = "Python is a programming language"

print(str1)

substring = str1[7:9]
print(substring)

substring = str1[24:32]
print(substring)

substring = str1[:6] # bydefault it considers starting range as 0
print(substring)

substring = str1[12:] # bydefault it will consider end of string
print(substring)

substring = str1[:]
print(substring)

substring = str1[-1:]
print(substring)

substring = str1[-8:-4]
print(substring)

substring = str1[1:6:2]
print(substring)

substring = str1[::-1]
print(substring)

str2 = input("Enter string : ")
rev = str2[::-1]
print(rev)
