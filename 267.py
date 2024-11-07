#modify object properties
#you can modify properties on objects like this

#set  the age of p1 to 40

class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person1(self):
        print("hello my name is " + self.name)

p1 = person("john",34)
p1.age = 40
print(p1.age)

