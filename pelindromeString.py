def checkPelindrome(x):
    y= x[::-1]
    if(y ==x):
       return True
    else:
        return False

x = input("enter any string: ")
print(checkPelindrome(x))