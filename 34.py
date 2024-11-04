#remove whitespace

#whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.


#the strip() method removes any whitespace from the begginning or the end:

a = "hello, world! "
print(a.strip())                #returns "hello, world"


b = ' what is your name;'

print(b.strip())
