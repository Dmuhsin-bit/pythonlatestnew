#customize sort function

#you can also customize your own function by
# using the keyword argument key = function.
#the function will return
# a number that will be used to sort the list ( the lower number first )

#sort the list based on how close the number is to 50?

def myfunc(n):
    return abs(n -50)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)



#myfunc(100) return abs(100-50) =50
#myfunc(50) return abs(50-50) =0
#myfunc(65) return abs(65-50) =15
#myfunc(82) return abs(82-50) =32
#myfunc(23) return abs(23-50) =27

#the list is sorted based on these returned values:
#50 (from 100)
#0 (from 50)
#15 (from 65)
#32 (from 82)
#27 (from 23)
#the sorted order of the list will be: [50,65,23,82,100],
#which corresponds to sorting by the absolute difference from 50.

