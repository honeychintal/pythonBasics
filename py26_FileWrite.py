def withWriteMode():
    """Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists"""
    f= open("filess\\WriteMode.txt","w")
    f.write("Hello I can write and overwrite")
    f.close()

def withAppendMode():
    """Opens a file for appending at the end of the file, Creates a new file if it does not exist"""
    f= open("filess\\AppendMode.txt","a") # writes to a file
    f.write("Hello I can write and append \n")
    f.close()

def withReadAndWriteMode():
    """Opens a file for reading and writing at same time"""
    f= open("filess\\ReadAndWriteMode.txt","r+") # writes to a file
    f.write(" Hello I can write and append in existing file")
    print(f.readline())
    f.close()

withWriteMode() #calling method withWriteMode()
withAppendMode() #calling method withAppendMode()
withReadAndWriteMode() #calling method withReadAndWriteMode()