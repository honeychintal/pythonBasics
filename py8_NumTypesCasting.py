var1= "30"
var2= "40"
var3= 50
var4= 99.99

print(var1+var2) # string concatination
print(var3+var4) # number addition
print(int(var2)+var3) #casting var2 as Integer to allow addition with int type var3
print(100 * (str(var4) +"\t")) #casting var4 as string and writing 100 times
print(isinstance(var4,float))