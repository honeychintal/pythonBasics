# dictionary is data structure that contains, key value pairs, keys and values can be of any type 
dict1 ={
        "zubin":["mango","banana","grapes"], # key is "string", and value is "list"
        "yaqub":["spinich","broccoli","ladyfinger"],
        "Xerbon":["chicken","prawns","fish","meat"],
        "worudo":["tofu","curd","cheese","fresh creame"],
        "vision":{"veg":"Butter Paneer","nonveg":"Butter Chicken"} # key is "string", and value is dictionary 
        }

print('dict1["zubin"][0] =',dict1["zubin"][0]) # 0th element of key "zubin"
print('dict1["yaqub"][::-1] =',dict1["yaqub"][::-1]) # all elements of "yaqub" in reverse order
print('dict1["vision"] =',dict1["vision"]) # dictionary of "vision"
print('dict1["vision"]["veg"] =',dict1["vision"]["veg"]) # value of "vision" of "veg"

dict2 ={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:["five","IV"]
        }
print('dict2[1] =',dict2[1])
print('dict2[5] =',dict2[5])
print('dict2[5][1] =',dict2[5][1])
print(dict2.items()) # returns key each key value pair as a tuple of a list
print(dict2.values()) # ignore keys and return a tuple of all the values of all keys
print(dict2.pop(2)) # deletes the item of specified key
print(dict2.keys()) # returns all the keys present in dictionary

dict2.update({2:"two"}) # update/insert the given key value to dictionary
print(dict2)

