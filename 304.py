#convert a python object containing all the legal data types?
import json

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
print(json.dumps(x))
