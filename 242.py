#function definition to make a function
# that always triples the number you send in ?

#lambda functions

#function definition to make a function
#that always doubles the number you send in ?


#function definition:
def myfunc(n):
    return lambda a : a * n

#creating a multiplier:
mydoubler = myfunc(3)

print(mydoubler(11))
