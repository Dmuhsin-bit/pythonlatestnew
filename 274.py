#add properties
#add a property called graduationyear to the student class ?


class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear = 2019

x = student("ilyas","rizwan")
print(x.graduationyear)

