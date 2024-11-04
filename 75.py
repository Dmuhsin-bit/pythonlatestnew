#without list comprehension
#you will have to write a for statement with a conditional test inside :

fruits = ["apple", "banana","cherry","kiwi","mango"]
newlist = []

for x in fruits :
    if "a" in x:
        newlist.append(x)

print(newlist)


#using list comprehension

fruits = ["apple", "banana","cherry","kiwi","mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)