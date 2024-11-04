#acceess items in nested dictionaries

#print the name of child 2
myfamily = {
 "child1"  : {
    "name" : "email",
    "year" : 2011
},
 "child2"  : {
    "name" : "tobias",
    "year" : 2007
},
 "child3"  :{
    "name" : "linus",
    "year" : 2011
}
}

print(myfamily["child2"]["name"])
