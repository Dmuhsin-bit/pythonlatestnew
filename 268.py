#delect object properties

#you can delete properties on objects by using the del keyword:
#delete the age property from the p1 object ?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person1(self):
        print(("hello my name is "+ self.name))

p1 = person("john",34)

del p1.age
print(p1.age)
