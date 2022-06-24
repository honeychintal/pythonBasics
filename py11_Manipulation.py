numers=[] #Empty list, Lists are Mutable
numers.append("X") #append method is used to add new element in the end of list
numers.append("Y")
numers.append("Z")
numers.append(100)
print(numers) #print after append

numers.insert(1,"y") #inserts given object at given index and shifts other elements one index further
print(numers)

numers[4]="sigma" #inserts given object at given index but replaces element present in given index
print(numers)

numers.pop() #deletes the last index object present in list
print(numers) 

numers.remove("y") # Remove first occurrence of value
print(numers)
