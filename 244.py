# Create a Python function, power_of,
# that takes one argument n and returns a lambda function
# that raises any number passed to it to the power of n.
# Use this function to create square,
# a function that squares any number.
# Test it by squaring the number 4.


def powerof(n):
    return lambda a : a**n
square = powerof(2)

print(square(6))
