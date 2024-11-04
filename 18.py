#local variable

def myfunc1():
    z="super"
    #z is an local variables, can be accessed only inside function.
    print(z)

myfunc1()
#global keyword
x="beutiful"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("python is "+x)
