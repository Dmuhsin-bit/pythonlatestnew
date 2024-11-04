#global variables

#create a variable outside of a function, and
# use it inside the function & outside the function.

x = "awesome"


def myfunc():
    print("python is "+ x)

myfunc()
print(x)

