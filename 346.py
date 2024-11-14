#read only parts of the file

#by default the read() method returns the whole text,

# but you can also specify how many characters you want to return:

#return the 5 first characters of the file ?

f = open("demo file.txt","r")
print(f.read(5))
