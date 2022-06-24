"""File IO basics
"r" - Opens a file for reading. (default) 
"w" - Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
"x" - Opens a file for exclusive creation. If the file already exists, the operation fails
"a" - Opens a file for appending at the end of the file, Creates a new file if it does not exist
"t" - Opens in text mode. (default)
"b" - Opens in binary mode.
"+" - Opens a file for updating (reading and writing)
"""
f = open("filess\TOD.txt") #open() returns the file pointer
print(f.read()) #file pointer can be used for file operations
f.close() #close() releases the resources used for file operations

f = open("filess\TOD.txt","rb") #reading file in 'byte' mode
for line in f.readlines(): # .readlines() iterates file in line by line 
    print(line ,end="<---\n")
f.close()