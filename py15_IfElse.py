age = int(input("Enter your Age: "))
if(age>18 and age<90):
    print("You can Drive, and BE SAFE")
elif(age<18):
    print("You cannot drive, GO HOME")
elif(age==18):
    print("Cannot decide, you have to pass Accessment")
else:
    print("Its not your age to Drive,TAKE REST")
