#pyuthon iterations

# an iterator is an object that contains a countable number of values ,

# an iteration is an object which consist of the methods
#_iter() and __next_().

#return the iterator from a tuple , and printbeach value ?

mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))