def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
try:
    num = int(input("please enter a non negative integer: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        result = sum_of_digits(num)
        print(f"The sum of the digits of {num} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
