num=input("enter a number: ")

if(num.isdigit()):
    print("Its a number")
    if(num.__contains__('.')):
        print("float number")
    elif(not num.__contains__('.')):
        print(type(int(num)))
elif(num.isalnum()):
    print(num," is alphanumeric")