#another way to make a copy is to use the built-in function dict().

#make a copy of a dictionary with the dict() function:

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
mydict = dict(thisdict)
print(mydict)
