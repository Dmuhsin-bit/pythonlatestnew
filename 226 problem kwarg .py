#Write a Python function called describe_person
# that can take any number of keyword arguments about a person.
# The function should print each key-value pair
# in the format: "[key]: [value]".
# If no information is provided,
# the function should print "No details available."
# Call the function with the arguments
# name="Alice", age=30, and city="New York".


#name: Alice
#age: 30
#city: New York

def describe_person(**details):
    if not details:
        print("no details available")
    else:
       for key , value in details.items():
        print(f"{key}:{value}")
describe_person(name = "alice",age = 30, city = "new york")


