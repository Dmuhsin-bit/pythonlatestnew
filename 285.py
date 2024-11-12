#class polymorphism

#polymorphism is often used in class methods,
#where we can have multiple classes with the same method name.

#different classes with the same method ?

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")
class boat:
        def __init__(self, name, type):
            self.name = name
            self.type = type

        def move(self):
            print("sail")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

car1 = car("ford",2021)
boat1 = boat("bmw","classic")
plane1 = plane("indigo","india")

for x in (car1,boat1,plane1):
    x.move()


