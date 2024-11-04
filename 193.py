# check if a number x is between two other numbers y and z (inclusive).
# Additionally, check if x is not equal to a given number k.

#Use and to ensure x is between y and z.
#Use not to ensure x is not equal to k.
#Use or to add an alternative condition
# that will pass if x is exactly twice the value of k.
#If the conditions are met,
# print "Conditions are met!",
# otherwise print "Conditions are not met!".


x = 12
y = 10
z = 30
k = 16
if (y <= x <= z and x != k) or x == 2 * k:
    print("conditons are met")
else:
    print("conditions are not met")

