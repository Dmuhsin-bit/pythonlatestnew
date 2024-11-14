#many exceptions

#you can defined as many exception blocks as you want,
#e.g if you want excute a special block of code
#for a special kind of error :

#print one message if the try block raises a name error
# and another for other errors?

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
    
