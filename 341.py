#In Python, map(), filter(), and reduce() are higher-order functions
#that allow you to perform operations on iterables like lists, tuples, etc.
# They are especially useful for functional programming
# as they help apply transformations, filtering, and
# reductions to collections in a concise way.


# The map() function
# The map() function applies a specified function to each item
# in an iterable (such as a list or tuple)
# and returns an iterator with the results.


#Syntax

#  map(function, iterable)

#function: The function to apply to each element in the iterable.
#iterable: The collection of items
# (e.g., list, tuple) to apply the function to.




# Squaring each element in a list.

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x **2, numbers))
print(squared_numbers)
