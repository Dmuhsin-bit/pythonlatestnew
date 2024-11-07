# Create a method in the Animal class.
# Insert a function that prints the animal's name and sound,
# and execute it on the a1 object.
class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def animal1(self):
        print(f"animal name:{self.name} animal {self.sound}")

a1 = animal("rizwan","grrrrr")

a1.animal1()

