# Write a Python function, power_func,
# that takes one argument n and returns a lambda function
# that raises any number passed to it to the power of n.
# In the same program, create both square and cube functions using power_func.
# Test them by squaring the number 5 and cubing the number 3.
def powerfunc(n):
    return lambda a : a**n

square = powerfunc(2)
cube = powerfunc(3)

print(square(5))
print(cube(3))
