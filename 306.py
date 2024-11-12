#You can also define the separators,
import json

# default value is (", "     ": "),

# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator ?


x ={
    "name":"john",
    "age":30,
    "married":True,
    "divorsed":False,
    "children":("ann","billly"),
    "pets":None,
    "cars":[
        {"model":"bmw 230","mpg":27.5},
        {"model":"ford edge","mpg":24.1}
    ]
}
print(json.dumps(x,indent=4, separators=(".","=")))
