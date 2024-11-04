#the intersection_update() method

# will also keep only the duplicates,
#but it will change the original set instead of returning a new  set.

#keep the items that exist in both set1, and set2 ?

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.intersection_update(set2)
print(set1)
