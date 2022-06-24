# Set is an unordered collection of unique items.
myset1= {1,2,3,4,5}
myset2={"Q","w","E","R","T","T","Y","T","t"} # set will ignore the repeated objects
myset3= {3,4,5,6,7}
print(myset1)
myset1.add(6)
myset1.add(6) # set does not allow duplicate objects
print(myset1)
print(myset2)
print(myset1.intersection(myset3)) # returns the intersection of the set
print(myset1.union(myset3)) # returns the union of the set

"""remove() is different from the discard() method, 
    because the remove() method will raise an error if 
    the specified item does not exist, and the discard() method will not"""
myset2.discard("t")
print(myset2)
myset2.remove("T")
print(myset2)