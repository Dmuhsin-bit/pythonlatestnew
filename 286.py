#inhertance class polymorphism

#the class classes inherits the vehicle methods

#create a class called vehicle and make
#car, boat, plane child classes of vehicle ?

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move (self):
        print("move")
class car(vehicle):
    pass

class boat(vehicle):

    def move(self):
        print("sail")

class plane(vehicle):
    def move(self):
        print("fly")

car1 = car("ford","mustang")#create a car object
boat1 = boat("ibiza","touring 20")#create a boat object
plane1 = plane("indigo","747")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
