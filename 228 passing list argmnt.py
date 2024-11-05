#Passing a List as an Argument

#You can send any data types of argument to a function
# (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# if you send a List as an argument,
# it will still be a List when it reaches the function:

def myfunction(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]

myfunction(fruits)
