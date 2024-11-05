#recursion
#python also accepts function recursion,
#which means a defined function can call itself.

#example of a recursive function-

def factorial(x):
    if x == 1 :
        return 1
    else:
        return (x * factorial(x - 1))

num = 4
print("the factorial of", num, "is", factorial(num))
#factorial of 3 = 1*2*3 = 6


