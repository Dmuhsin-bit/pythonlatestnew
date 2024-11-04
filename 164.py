# remove dictionary items


#removing items
#there are several methods to remove items from a dictionary

#the pop() method removes  the item with the specified key name:

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
thisdict.pop("model")

print(thisdict)
