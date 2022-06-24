import constant as con

def docstringmethod():
    """Hello I am docstring of method docstringmethod """
    var1="this contains a string"
    var2=10
    var3=99.99999
    return var2+var3

def multiValueAssign():
    a,b,c,d,e,f=1,2,3,4,5.5,"six"
    return (a,b,c,d,e,f)


def sameValueAssign():
    x = y = z = "'#SameBeef'"
    print("x= ",x,"y= ",y,"z= ",z)

#Calling all defined methods
print(docstringmethod.__doc__)
print(docstringmethod())
print(multiValueAssign())  
sameValueAssign()
print(con.GRAVITY)
print(con.PI)