a,b =20,30
c=sum((a,b)) #sum is built in function, it takes iterables of numerical values as parameter and returns sum of all numbers
print(c)

def function1(): 
    """This function takes no arguments and not returns anything"""
    print("I am function1, I return NOTHING:")

def function2(name): 
    """This function takes one argument and not returns anything"""
    print("I am function2, I can print your name ",name)

def function3(x,y): 
    """This function takes two argument and returns sum of arguments"""
    print("I am function3, I return the Sum of numbers ")
    return x+y

def function4(x,y=0): 
    """This function takes two argument where default value of y is '0' and returns sum of arguments"""
    print("I am function4, I return the Sum of numbers, default value of y is '0' ")
    return x+y

def function5(*x):
    """This function takes n number arguments"""
    print("I am function5, I take multiple arguments as a tuple, and return sum")
    return sum(list(x)) 

print(function1()) # This method returns null, and takes no arguments
print(function1.__doc__) #This returns the docstring of the method
print(function2("Raju")) 
print(function3(10,30)) #passing numbers will do the addition
print(function3("10","30")) #passing strings will do the concatination
print(function4(10)) #passing only value of x, and method will use default value of y
print(function4(10,90)) #passing only value of x and y, method will use the passed value of y
print(function5(1,2,3,4,5)) # arguments get wrapped up into a tuple before being passed into the function.