# OrderedDict

# it's a child class of dict class
# it remembers the order in which the key was inserted

from collections import OrderedDict

ordereddict_obj = OrderedDict()
ordereddict_obj["a"] = "Aaditya"
ordereddict_obj["b"] = "Bharati"
ordereddict_obj["c"] = "Chaitali"

print(ordereddict_obj)
 
print(ordereddict_obj["b"])