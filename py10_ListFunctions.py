
from pickle import TRUE


shampoo=["Garnier","Patanjali","Tresemme","Sunsilk","Dove"] #lists are mutable, it changes when list methods are applied on them
print(shampoo) # print complete list
print(shampoo[4]) # print 4th index element from list
print(shampoo[:3]) # print 0 to 3rd index elements in list
print(shampoo[::-1]) # reverse the list
print(shampoo[::2]) # print every 2nd element of list

numberss=[-9,54,69,0,78,-33,58,49,100,665,878]
print(numberss) 
numberss.reverse() # arrange the elements of list in reverse 
print(numberss)
numberss.sort() # arrange the numbers of list, in ascending order 
print(numberss)
numberss.sort(reverse=True) # arrange the numbers of list, in descending order
print(numberss)
#----------------------------------
print(max(numberss)) # print the maximum number in the list
print(min(numberss)) # print the minimum number in the list
print(len(numberss)) # print the count number in the list
#----------------------------------
