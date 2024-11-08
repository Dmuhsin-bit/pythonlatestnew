#add properties
# add a property called 'position' to the 'employee' class

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class employee(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.position = "software engineer"

x = employee("ilyas","rizwan")
print(x.position)

