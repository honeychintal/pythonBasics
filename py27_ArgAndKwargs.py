def argsMethod(*args):
    print(sum(args))

def kwargsMethod(**kwargs):
    for key,valu in kwargs.items():
        print(key +" is "+valu)

argsMethod(10)
argsMethod(10,20)
argsMethod(10,20,30)

kwargsMethod(name="Raj")
kwargsMethod(name="Suraj", proffession="Teacher")
kwargsMethod(name="Maharaj", proffession="King", age="55")


