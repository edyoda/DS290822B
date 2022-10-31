import re

# data = "HELLO"
# res = re.findall("[a-z]",data) # pattern, data  # checks for small letters
# print(res)

# data = "HELLO"
# res = re.findall("[A-Z]",data) # checks for capital letters
# print(res)

# data = "Hello123"
# res = re.findall("[A-z]",data) # considers both capital and small
# print(res)

# data = "HELLO"
# res = re.findall("[a-zA-Z]",data) # considers both capital and small
# print(res)

# data = "Hello"
# res = re.findall("[d-h]",data) # checks characters from d - h
# print(res)

# data = "HELLO"
# res = re.findall("[D-H]",data) # checks characters from D - H
# print(res)

# data = "Hello123"
# res = re.findall("\d",data) # checks for digits
# print(res)

# data = "Python is a programming language"
# res = re.findall("is|language|Python|Bharati",data) # checks for is|language|Python|Bharati
# print(res)

# data = "Hello Bharati"
# res = re.findall("H...o",data) # search for the word which starts with 'H' and ends with 'o' and inbetween it has 3 characters
# print(res)

# data = "Hello Bharati"
# res = re.findall("H.*o",data) # search for the word which starts with 'H' and ends with 'o' and inbetween 0 or more characters
# print(res)

# data = "Hello Bharati"
# res = re.findall("H.+o",data) # search for the word which starts with 'H' and ends with 'o' and inbetween 1 or more characters
# print(res)

# data = "Hlo Bharati"
# res = re.findall("H.?o",data) # search for the word which starts with 'H' and ends with 'o' and inbetween 0 or 1 character
# print(res)

# data = "Hello Bharati"
# res = re.findall("Bharati",data) # checks for Bharati
# print(res)

# data = "Helleeo Bharati"
# res = re.findall("H.{5}o",data) # search for the word which starts with 'H' and ends with 'o' and inbetween 5 characters
# print(res)

# data = "Hello Bharati"
# res = re.findall("^Hel",data) # checks if string starts with 'Hel'
# print(res)

# data = "Hello Bharati"
# res = re.findall("arati$",data) # search for the word which starts with 'H' and ends with 'o' and inbetween 0 or more characters
# print(res)

