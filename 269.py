#delete object

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def person1(self):
        print(("hello my name is "+ self.name))

p1 = person("john",34)

del p1
print(p1)

