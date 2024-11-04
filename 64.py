#add any iterable

#the extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).

#add elements of a tuple to a list?

thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)
