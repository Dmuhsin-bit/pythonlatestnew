#loop through both keys and values,
#by using the items() method:

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for x,y in thisdict.items():
    print(x,y)
    