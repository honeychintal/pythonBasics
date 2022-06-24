mystr ="Save your tears for another day!!"
mystr_len = len(mystr) # length of string

print(mystr[0:]) # 0 to all the characterts available in the String
print(mystr[:mystr_len]) # by default from 0 to length of string
print(mystr_len) # print length of string, its 33
print(mystr[0:33]) # print from index 0 to index 33 in the String
print(mystr[::2]) # ignore every 2nd character of string, by default 3rd parameter value is 1
print(mystr[::3]) # ignore every 3rd character of string
print(mystr[:]) # by default 1st val contains 0, 2nd contains length and 3rd contains 1
print(mystr[-5:]) # print -5 index till the length of string
print(mystr[::-1]) # print characters in reverse order
"""STRING METHODS"""
print(mystr.index("for")) # returns the index of the substring passed
print(mystr.split("e")) # split the string based on given pattern, and returns lists of splitted words
print(mystr.replace("tears","soul")) #replace old substring with new substring
print(mystr.swapcase()) # swaps the case of all the characters
print(mystr.upper()) # returns string as uppercase
print(mystr.count("r")) #number of times the character appeared in string