# Counter

# it a class from collection module
# it's a child class of dict class
# it will conside the element as key and the count of element as value


# ["a","a","b","a","c","c"]
# a : 3
# b : 1
# c : 2

from collections import Counter

lst = ["a","a","b","a","c","c"]

counter_obj = Counter(lst)
print(counter_obj)

counter_obj = Counter(a=4,b=9,c=10)
print(counter_obj)

counter_obj = Counter({'a':3,'b':2,'c':1})
print(counter_obj)