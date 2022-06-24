# tuples are immutable, therer is no assignments can be done
tuppl =(1,2,3,"amul","fresh","fresh","creme")
leest =["no"]
leest[0]="yo" # Allowed, on list
# tuple[0]=100 # Not Allowed! on tuple, TypeError: 'type' object does not support item assignment
print(tuppl)
print(leest)