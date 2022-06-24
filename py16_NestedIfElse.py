'''Program to check number is +ve, -ve or zero, with "nested IF"'''
num=int(input("enter a number: "))

if (num>=0):
    if num==0:
        print("number is ZERO")
    else:
        print("number is +VE")
else:
    print("number is -VE")