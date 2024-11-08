# Add a salary parameter,
# and pass the correct salary when creating objects.
# Use the Employee class to create an object with the specified salary,
# and then print the salary property:
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class employee(person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary

x = employee("ilyas","rizwan",20000)
print(x.salary)
