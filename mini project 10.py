def factorial(n):
    if n < 0:
        return "factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *=1
        return result
sahal = int(input("enter a non negative integer:"))
factorial_result = factorial(sahal)
print(f"factorial of {sahal} is {factorial_result}")

