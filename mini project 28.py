def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base} to the power of {exponent} is {result}")
