def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
try:
    num1 = int(input("10: "))
    num2 = int(input("20: "))

    gcd = find_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {gcd}")

except ValueError:
    print("Please enter valid integers.")
