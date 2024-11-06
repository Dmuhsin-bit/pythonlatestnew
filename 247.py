# Write a Python function, make_calculator,
# that takes one argument n and returns a lambda function
# that adds n to any number passed to it.
# In the same program, create both add_ten and subtract_five functions
# using make_calculator.
# Test them by adding 10 to the number 7 and
# subtracting 5 from the number 20.

def makecalculator(n):
    return lambda a : a + n

addten = makecalculator(10)
subtractfive = makecalculator(-5)

print(addten(7))
print(subtractfive(20))
