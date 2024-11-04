#the symmetric_difference_update() method
#will also keep all but the duplicates,
#but it will change the orginal set instead of returning a new set.


#use the symmetric_difference_update() method to
#keep the items that are not present in both sets ?

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1)
