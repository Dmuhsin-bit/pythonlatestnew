##The reduce() function,
# from the functools module,
# applies a function cumulatively to the elements in an iterable,
# reducing it to a single value.


#Syntax

# from functools import reduce
# reduce(function, iterable)

#function: A function with two arguments,
# which will be applied cumulatively to the items.
#iterable: The collection of items to reduce.

#calculating the product of all elements in a list

from functools import reduce

numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x * y,numbers)
print(product)
