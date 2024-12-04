def divide_numbers(a, b):
    try:
        result = a / b  # Attempt to divide
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
divide_numbers(10, 0)
divide_numbers(10, 2)
