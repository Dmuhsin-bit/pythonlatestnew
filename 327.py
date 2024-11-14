#else

#you can use the else keyword to defined a block of code to be executed
#if no errors were raised:

#in this example, the try block does not generate any errors !

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
    