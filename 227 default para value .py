#Default Parameter Value

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def myfunction(country = "norway"):
    print("i am from" + country)

myfunction("sweden")
myfunction("india")
myfunction()
myfunction("brazil")

