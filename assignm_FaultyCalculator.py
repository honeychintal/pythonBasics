# 45*3 =555, 56+9=77, 56/6=4
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
oprt = input("Operator: ")

if(num1==45 and num2==3 and oprt=="*"):
    print(555)
elif(num1==56 and num2==9 and oprt=="+"):
    print(77)
elif(num1==56 and num2==6 and oprt=="/"):
    print(4)
elif(oprt=="+"):
    print(num1 +num2)
elif(oprt=="-"):
    print(num1 -num2)
elif(oprt=="/"):
    print(num1 /num2)
elif(oprt=="*"):
    print(num1 *num2)
else:
    print("something went wrong!!")
