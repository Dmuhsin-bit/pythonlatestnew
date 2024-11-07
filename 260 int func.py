#The _init_() Function
#the built-in _init_() function.
#All classes have a function called _init_(),
# which is always executed when the class is being initiated.
#Use the _init_() function
# to assign values to object properties,
# or other operations that are necessary
# to do when the object is being created:

# Create a class named Person ?
# use the _init_() function to assign values for name and age ?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("john",36)

print(p1.name)
print(p1.age)

#The _init_() function is called automatically
# every time the class is being used to create a new object.
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.

