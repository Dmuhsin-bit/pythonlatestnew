#Python Inheritance

#Inheritance allows us to define a class that inherits all the methods
# and properties from another class.

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class,
# also called derived class.

#Create a Parent Class

#Create a class named Person,
# with firstname and lastname properties, and a printname method:

class person :
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname =lname
    def printname(self):
        print(self.fname,self.lname)

#use the person class to create an object,
#and then execute the printname method:

x = person("john","rizwan")

x.printname()

class student(person):
    pass

#Note: Use the pass keyword when you do not want to add any other properties
# or methods to the class.

#Now the Student class has the same properties and methods as the Person class.

#Use the Student class to create an object,
# and then execute the printname method:

s1 = student("illyas","liyan")
s1.printname()
