#the values true and 1 are considered the same value.
#the same goes for false and 0

#join sets that contains the values
#true, false,1,and 0, and see what is considered as duplicates?

set1 = {"apple",1,"banana",0,"cherry"}
set2 = {"google",False,1,2,"apple",True}


set3 = set1.intersection(set2)

print(set3)