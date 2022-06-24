# range generates sequence from 0 to given number

for i in range(100):
    print(i,end= ", ")
print('\n')

# geneates the multiplication table of 3
for i in range(0,33,3): # '0' is starting number of sequence, '33' is ending of sequence, '3' is step 
    print(i,end= ", ")
print('\n')

for i in range(97,123):
    print(chr(i), end= ", ") # generates alphabets based on ascii values
print('\n')

# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
