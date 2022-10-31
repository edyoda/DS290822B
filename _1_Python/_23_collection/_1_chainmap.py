# ChainMap
# it a class from collection module
# used to combine multiple dictionary together
# it returns us the combined dictionary of all dictionary

from collections import ChainMap

dict1 = {"a":"A","b":"B","c":"C"}
dict2 = {"d":"D","e":"E","j":"Rahul"}
dict3 = {"g":"H","i":"I","j":"Bharati"}

chain_map_obj = ChainMap(dict1,dict2,dict3)
print(chain_map_obj)
print(type(chain_map_obj))
print(chain_map_obj["j"])

print(chain_map_obj.keys())
print(chain_map_obj.values())

dict4 = {"x":"X","y":"Y"}
chain_map_obj = chain_map_obj.new_child(dict4)
print(chain_map_obj)