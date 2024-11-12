#convert from python to json
#if you have a python object,

#you can convert into a json string by
#using the json.dump() method.

#convert from python to json?
import json
# a python object (dict)
x = {
    "name":"john",
    "age": 30,
    "city":"new york"
}
#convert into json
y = json.dumps(x)
#the result is a json string:
print(y)
