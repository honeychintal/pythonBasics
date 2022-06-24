num=15
guess=5
while(guess>0):
    guess=guess-1
    print("only '",guess,"' GUESS left")
    inp_num=int(input("Enter number: "))
    if(num<inp_num):
        print("your number is GREATER +++++")
        continue
    elif(num>inp_num):
        print("your number is SMALLER -----")
        continue
    elif(num==inp_num):
        print("@ # $ % ^ * _ + You won, You guessed it Correct @ # $ % ^ * _ +")
        break
else:
    print(":( :( :( :( You Lose :( :( :( :(")
    