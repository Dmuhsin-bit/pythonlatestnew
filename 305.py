#Format the Result
#Use the indent parameter to define the numbers of indents ?
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
print(json.dumps(x,indent=4))

#use four indents to make it easier to read the result:
