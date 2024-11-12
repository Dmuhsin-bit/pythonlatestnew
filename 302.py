#Parse JSON - Convert from JSON to Python

#If you have a JSON string,
# you can parse it by using the json.loads() method.

#The result will be a Python dictionary.

# Convert from JSON to Python?

import json

#some json:
x = '{"name":"john","age":30,"city":"new york"}'

#parse x :
y = json.loads(x)

#the result is a python dictionary:

print(y)


