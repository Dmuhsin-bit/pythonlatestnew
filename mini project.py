def greatest_num(a,b,c):
    if a>=b and a>=c :
        return a
    elif b>= a and b>=c:
        return b
    else:
        return c
try:
    greatest = greatest_num(23,25,32)
    print(f"the greatest number is: {greatest}")
except ValueError:
    print("invalid input")
