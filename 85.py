#perform a case-insensitive sort of the list:

thislist = ["banana","orange","kiwi","cherry"]

thislist.sort(key = str.lower)

print(thislist)

#the key parameter is set to str.lower,
#which means that the list will be sorted based
#on the lowercase version of each string element.


#"banana" . lower() returns "banana"
#"orange" . lower() returns "orange"
#"kiwi" . lower() returns "kiwi"
#"cherry" . lower() returns "cherry"