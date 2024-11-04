#Write a Python program to determine
# the type of a triangle
# based on the lengths of its three sides (a, b, and c).

#First, check if the three sides form a valid triangle:
#A triangle is valid if the sum of any two sides is greater
# than the third side.
#If it is a valid triangle, check the following conditions:
#If all three sides are equal, print "Equilateral Triangle".
#If only two sides are equal, print "Isosceles Triangle".
#If no sides are equal, print "Scalene Triangle".
#If the sides do not form a valid triangle, print "Not a Triangle".


a = 5
b = 5
c =  8

if a+b > c and a+c > b and b+c > a:
    if a == b == c:
        print("equilateral triangle")
    elif a == b or a ==c or b == c:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("not triangle")


