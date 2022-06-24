n = int(input("Enter no. of lines for pattern: "))
pat_type = bool(int(input("enter [1] for 'incremental' pattern, or enter [0] of 'decremental' pattern :")))
print(pat_type)
if(pat_type==True):
    for i in range(1,n+1):
        print(i*"*")
else:
    for i in range(-n,1):
        print("*"*abs(i))