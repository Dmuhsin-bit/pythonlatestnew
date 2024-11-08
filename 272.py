#Add the _init_() Function to child class

#So far we have created a child class that inherits the properties
# and methods from its parent.

#We want to add the _init_() function to the child class
# (instead of the pass keyword).

# The _init_() function is called automatically every time the class
# is being used to create a new object.


#Add the _init_() function to the Student class ?

#When you add the _init_() function,
# the child class will no longer inherit the parent's _init_() function.

# The child's _init_() function overrides
# the inheritance of the parent's _init_() function.

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

x = student("ilyas","rizwan")
x.printname()



