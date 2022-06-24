x,y=10,0
try: #try contains the statement that may encounter an exception
    print(x/y) 
except Exception as e: #except block is invoked if exception occured
    print(e)
finally:
    print("I am FINAL") #finally clause is executed no matter what