#The self Parameter!
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
#It does not have to be named self ,
# you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
# Use the words mysillyobject and abc instead of self ?

class person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age =age

    def person1(abc):
        print("hello my name is " + abc.name)
p1  = person("name",34)
p1.person1()
