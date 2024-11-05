#Write a Python function called describe_pet
# that takes two keyword arguments: animal_type and pet_name.
# The function should print a sentence describing
# the pet in the format: "I have a [animal_type] named [pet_name]."
# Call the function with the arguments animal_type="dog" and pet_name="Buddy".


#I have a dog named Buddy.

def describe_pet(typ,name):
    print(f"I have a {typ} named {name}")
    return

#describe_pet("dog","Buddy")
describe_pet(name="Buddy",typ="dog")